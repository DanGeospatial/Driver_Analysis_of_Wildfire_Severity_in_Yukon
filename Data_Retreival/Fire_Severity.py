"""
Wildfire severity was calculated using LandTrendR
"""
from osgeo import gdal


def getdNBR(area, fire_id, savepath):
    file_dnbr = ("D:/Research/Masters/4_Model_Files/Fire History/Fires/dNBR LTR1_5/" + fire_id + "/" + "dNBR_" + fire_id
                 + ".tif")

    bounds = gdal.Open(area, gdal.GA_ReadOnly)
    dataset = gdal.Open(file_dnbr, gdal.GA_ReadOnly)

    output = gdal.Warp(savepath + ".tif", dataset,
                       outputBounds=[bounds.xmin, bounds.ymin, bounds.xmax, bounds.ymax])

    output.close()
    dataset.close()
