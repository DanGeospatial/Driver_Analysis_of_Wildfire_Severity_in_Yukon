"""
Load land cover and clip
"""
import whitebox_tools

wbt = whitebox_tools.WhiteboxTools()
wbt.set_whitebox_dir("E:/Users/speed/anaconda3/envs/Yukon_Wildfire_Drivers_v2/Library/bin")


def getLC(area, savepath):
    file_mnbr = "I:/Wildfire_Aligned_Rasters_v2/CAN_LC_2020_Proj_Clip.tif"
    save_loc = savepath + "_LC" + ".tif"

    wbt.clip_raster_to_polygon(i=file_mnbr, polygons=area, output=save_loc)

