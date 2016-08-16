#-*- coding: utf-8 -*-

import shapefile
import geopandas as gpd
from geopandas import GeoDataFrame
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 도, 특별시, 광역시
e = shapefile.Editor('shapefiles/CTPRVN/TL_SCCO_CTPRVN')

for r in e.records:
    r[2] = unicode(r[2], 'euc-kr')

e.save('shapefiles/CTPRVN/TL_SCCO_CTPRVN_UNICODE')

g = GeoDataFrame.from_file('shapefiles/CTPRVN/TL_SCCO_CTPRVN_UNICODE.shp', encoding='utf-8')
g.crs = {'init':'epsg:5178'}

g.to_crs(epsg='4326', inplace=True)
g.to_file('shapefiles/CTPRVN/TL_SCCO_CTPRVN_UNICODE_4326.shp', encoding='utf-8')


# 시, 군
e = shapefile.Editor('shapefiles/SIG/TL_SCCO_SIG')

for r in e.records:
    r[2] = unicode(r[2], 'euc-kr')

e.save('shapefiles/SIG/TL_SCCO_SIG_UNICODE')

g = GeoDataFrame.from_file('shapefiles/SIG/TL_SCCO_SIG_UNICODE.shp', encoding='utf-8')
g.crs = {'init':'epsg:5178'}

g.to_crs(epsg='4326', inplace=True)
g.to_file('shapefiles/SIG/TL_SCCO_SIG_UNICODE_4326.shp', encoding='utf-8')

# 읍, 면, 동
e = shapefile.Editor('shapefiles/SIG/TL_SCCO_EMD')

for r in e.records:
    r[2] = unicode(r[2], 'euc-kr')

e.save('shapefiles/EMD/TL_SCCO_EMD_UNICODE')

g = GeoDataFrame.from_file('shapefiles/EMD/TL_SCCO_EMD_UNICODE.shp', encoding='utf-8')
g.crs = {'init':'epsg:5178'}

g.to_crs(epsg='4326', inplace=True)
g.to_file('shapefiles/EMD/TL_SCCO_EMD_UNICODE_4326.shp', encoding='utf-8')
