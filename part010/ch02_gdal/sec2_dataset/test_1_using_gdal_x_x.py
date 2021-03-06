#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import gdal
###############################################################################
from osgeo import gdal
###############################################################################
import gdal
###############################################################################
try:
    import gdal
except:
    from osgeo import gdal
###############################################################################
from osgeo.gdalconst import *
###############################################################################
gdal.AllRegister()
###############################################################################
driver = gdal.GetDriverByName('HFA')
driver.Register()
###############################################################################
driver = gdal.GetDriverByName('GeoTiff')
driver == None
###############################################################################
drv_count = gdal.GetDriverCount()
drv_count
###############################################################################
for idx in range(10):
    driver = gdal.GetDriver(idx)
    print( "%10s: %s" % (driver.ShortName, driver.LongName))

