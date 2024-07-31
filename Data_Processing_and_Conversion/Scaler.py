"""
Resample a raster to 30m
"""

import rasterio
from rasterio.enums import Resampling


def resample_nearest(raster):
    input_raster = rasterio.open(raster + ".tif")
    output_name = raster + "_ rs" + ".tiff"

    output = gdal.Warp(output_name, input_raster, xRes=30, yRes=30, resampleAlg="GRA_NearestNeighbour")

    output.close()
    input_raster.close()


def resample_cubic(raster):
    input_raster = gdal.Open(raster + ".tif", gdal.GA_ReadOnly)
    output_name = raster + "_ rs" + ".tiff"

    output = gdal.Warp(output_name, input_raster, xRes=30, yRes=30, resampleAlg="GRA_Cubic")

    output.close()
    input_raster.close()
