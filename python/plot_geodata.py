#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import geopandas as gpd
from shapely.geometry import Point
from geopandas import GeoDataFrame
import matplotlib
from matplotlib.pyplot as plt
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 한글 폰트 설정
krfont = {'family' : 'unbatang', 'weight' : 'bold', 'size'   : 10}
matplotlib.rc('font', **krfont)


geodata = gpd.GeoDataFrame.from_file('shapefiles/SIG/TL_SCCO_SIG_UNICODE_4326.shp', encoding='utf-8')

# 구분자 '^A'
data = pd.read_csv('data/sample.csv', sep='\x01', names=['latitude','longitude'])

data = GeoDataFrame(data, crs={'init':'epsg:4326'})
geometry = data.apply(lambda x: Point(x.longitude, x.latitude), axis=1)
data = data.set_geometry(geometry)
data.reset_index(inplace=True)

# 어떤 시, 군에 속하는지 알기 위해 조인한다.
data_with_geolocation = gpd.sjoin(data, geodata, how='inner', op='within')

counts = data_with_geolocation.SIG_CD.value_counts()
counts = counts.reset_index()
counts.columns = ['SIG_CD', 'total']
counts = counts.set_index('SIG_CD')

# 시, 군의 이름을 표시하기 위해 중심 위치의 좌표를 구한다.
counts['coords'] = counts['geometry'].apply(lambda x: x.representative_point().coords[:])
counts['coords'] = [coords[0] for coords in counts['coords']]

counts = GeoDataFrame(counts, crs={'init': 'epsg:4326'})

counts.plot(column='total', cmap='coolwarm')

for idx, row in counts.iterrows():
    plt.annotate(s=row['SIG_KOR_NM'], xy=row['coords'],
                 horizontalalignment='center')

sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=plt.Normalize(vmin=counts.total.min(), vmax=counts.total.max()))
sm._A = []
plt.colorbar(sm)

plt.show()