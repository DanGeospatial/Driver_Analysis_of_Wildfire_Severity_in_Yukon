"""
GRIB2 Utilities
"""


from osgeo import gdal


def gribUtils(gribFile, tiffPath):
    band = []
    outtype = "GTiff"

    # Open GRIB2
    grib = gdal.Open(gribFile)

    # Get band list
    for i in range(grib.RasterCount + 1):
        if i == 0:
            pass
        else:
            band.append(i)

    outTiff = gdal.Translate(tiffPath, grib, format=outtype, bandList=band)

    outTiff.close()
    grib.close()
