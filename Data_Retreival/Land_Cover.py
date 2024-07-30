"""
Load land cover and clip
"""
from osgeo import gdal


def mnbr(area, savepath):
    file_mnbr = "D:/Research/Masters/4_Model_Files/Ecology/Max Veg/mNBR.tif"

    bounds = gdal.Open(area, gdal.GA_ReadOnly)
    dataset = gdal.Open(file_mnbr, gdal.GA_ReadOnly)

    output = gdal.Warp(savepath + ".tif", dataset,
                       outputBounds=[bounds.xmin, bounds.ymin, bounds.xmax, bounds.ymax])

    output.close()
    dataset.close()

