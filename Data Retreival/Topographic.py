"""
These have been calculated locally using SAGA GIS for the Yukon
"""
from osgeo import gdal


def getAspect(area, savepath):
    file_aspect = "D:/Research/Masters/4_Model_Files/Topography/Aspect/Aspect_clip_Resample.tif"

    bounds = gdal.Open(area, gdal.GA_ReadOnly)
    dataset = gdal.Open(file_aspect, gdal.GA_ReadOnly)

    output = gdal.Warp(savepath + ".tif", dataset,
                            outputBounds=[bounds.xmin, bounds.ymin, bounds.xmax, bounds.ymax])

    output.close()
    dataset.close()


def getElevation(area, savepath):
    file_elevation = "D:/Research/Masters/4_Model_Files/Topography/No Sinks/Yukon_Elev_no_sinks_Resample.tif"

    bounds = gdal.Open(area, gdal.GA_ReadOnly)
    dataset = gdal.Open(file_elevation, gdal.GA_ReadOnly)

    output = gdal.Warp(savepath + ".tif", dataset,
                            outputBounds=[bounds.xmin, bounds.ymin, bounds.xmax, bounds.ymax])

    output.close()
    dataset.close()


def getSlope(area, savepath):
    file_slope = "D:/Research/Masters/4_Model_Files/Topography/No Sinks/Slope_clip_Resample.tif"

    bounds = gdal.Open(area, gdal.GA_ReadOnly)
    dataset = gdal.Open(file_slope, gdal.GA_ReadOnly)

    output = gdal.Warp(savepath + ".tif", dataset,
                            outputBounds=[bounds.xmin, bounds.ymin, bounds.xmax, bounds.ymax])

    output.close()
    dataset.close()


def getTWI(area, savepath):
    file_twi = "D:/Research/Masters/4_Model_Files/Topography/No Sinks/TopographicWetnessIndex_clip_Resample.tif"

    bounds = gdal.Open(area, gdal.GA_ReadOnly)
    dataset = gdal.Open(file_twi, gdal.GA_ReadOnly)

    output = gdal.Warp(savepath + ".tif", dataset,
                            outputBounds=[bounds.xmin, bounds.ymin, bounds.xmax, bounds.ymax])

    output.close()
    dataset.close()


def getTPI(area, savepath):
    file_tpi = "D:/Research/Masters/4_Model_Files/Topography/No Sinks/TopographicPositionIndex_clip_resample.tif"

    bounds = gdal.Open(area, gdal.GA_ReadOnly)
    dataset = gdal.Open(file_tpi, gdal.GA_ReadOnly)

    output = gdal.Warp(savepath + ".tif", dataset,
                            outputBounds=[bounds.xmin, bounds.ymin, bounds.xmax, bounds.ymax])

    output.close()
    dataset.close()
