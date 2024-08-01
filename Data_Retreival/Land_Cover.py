"""
Load land cover and clip
"""
import whitebox_tools

wbt = whitebox_tools.WhiteboxTools()


def mnbr(area, savepath):
    file_mnbr = "I:/Wildfire_Aligned_Rasters_v2/mNBR.tif"
    save_loc = savepath + ".tif"

    wbt.clip_raster_to_polygon(i=file_mnbr, polygons=area, output=save_loc)

