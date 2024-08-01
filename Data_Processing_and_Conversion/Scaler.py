"""
Resample a raster to 30m
"""

import whitebox_tools

wbt = whitebox_tools.WhiteboxTools()


def resample_nearest(raster):
    output_name = raster + "_ rs" + ".tiff"

    output = wbt.resample(inputs=raster, output=output_name, cell_size=30, method='nn')
    output.close()


def resample_cubic(raster):
    output_name = raster + "_ rs" + ".tiff"

    output = wbt.resample(inputs=raster, output=output_name, cell_size=30, method='cc')
    output.close()
