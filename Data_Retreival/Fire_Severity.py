"""
Wildfire severity was calculated using LandTrendR
"""
import whitebox_tools

wbt = whitebox_tools.WhiteboxTools()
wbt.set_whitebox_dir("E:/Users/speed/anaconda3/envs/Yukon_Wildfire_Drivers_v2/Library/bin")


def getdNBR(area, fire_id, savepath):
    file_dnbr = ("I:/Wildfire_Aligned_Rasters_v2/" + "dNBR_" + fire_id + ".tif")
    save_loc = savepath + "_dNBR" + ".tif"

    wbt.clip_raster_to_polygon(i=file_dnbr, polygons=area, output=save_loc)


def getmNBR(area, savepath):
    file_dnbr = ("I:/Wildfire_Aligned_Rasters_v2/" + "mNBR" + ".tif")
    save_loc = savepath + "_mNBR" + ".tif"

    wbt.clip_raster_to_polygon(i=file_dnbr, polygons=area, output=save_loc)


def getpre(area, year, savepath):
    year = int(year)
    year = year - 1
    file_pre = ("I:/Wildfire_Aligned_Rasters_v2/NBR_Fitted_" + str(year) + ".tif")
    save_loc = savepath + "_pre" + ".tif"

    wbt.clip_raster_to_polygon(i=file_pre, polygons=area, output=save_loc)
