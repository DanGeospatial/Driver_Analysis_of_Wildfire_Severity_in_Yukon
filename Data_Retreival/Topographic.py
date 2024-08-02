"""
These have been calculated locally using SAGA GIS for the Yukon
"""
import whitebox_tools

wbt = whitebox_tools.WhiteboxTools()
wbt.set_whitebox_dir("E:/Users/speed/anaconda3/envs/Yukon_Wildfire_Drivers_v2/Library/bin")


def getAspect(area, savepath):
    file_aspect = "I:/Wildfire_Aligned_Rasters_v2/Aspect_clip_Resample.tif"
    save_loc = savepath + "_Aspect" + ".tif"

    wbt.clip_raster_to_polygon(i=file_aspect, polygons=area, maintain_dimensions=True, output=save_loc)


def getElevation(area, savepath):
    file_elevation = "I:/Wildfire_Aligned_Rasters_v2/Yukon_Elev_no_sinks_Resample.tif"
    save_loc = savepath + "_Elevation" + ".tif"

    wbt.clip_raster_to_polygon(i=file_elevation, polygons=area, output=save_loc)


def getSlope(area, savepath):
    file_slope = "I:/Wildfire_Aligned_Rasters_v2/Slope_clip_Resample.tif"
    save_loc = savepath + "_Slope" + ".tif"

    wbt.clip_raster_to_polygon(i=file_slope, polygons=area, output=save_loc)


def getTWI(area, savepath):
    file_twi = "I:/Wildfire_Aligned_Rasters_v2/TopographicWetnessIndex_clip_Resample.tif"
    save_loc = savepath + "_twi" + ".tif"

    wbt.clip_raster_to_polygon(i=file_twi, polygons=area, output=save_loc)


def getTPI(area, savepath):
    file_tpi = "I:/Wildfire_Aligned_Rasters_v2/TopographicPositionIndex_clip_resample.tif"
    save_loc = savepath + "_tpi" + ".tif"

    wbt.clip_raster_to_polygon(i=file_tpi, polygons=area, output=save_loc)
