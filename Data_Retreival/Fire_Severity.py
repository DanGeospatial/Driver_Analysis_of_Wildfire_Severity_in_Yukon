"""
Wildfire severity was calculated using LandTrendR
"""
import whitebox_tools

wbt = whitebox_tools.WhiteboxTools()
wbt.set_whitebox_dir("E:/Users/speed/anaconda3/envs/Yukon_Wildfire_Drivers_v2/Library/bin")


def getdNBR(area, fire_id, savepath):
    file_dnbr = ("D:/Research/Masters/4_Model_Files/Fire History/Fires/dNBR LTR1_5/" + fire_id + "/" + "dNBR_" + fire_id
                 + ".tif")
    save_loc = savepath + "_dNBR" + ".tif"

    wbt.clip_raster_to_polygon(i=file_dnbr, polygons=area, maintain_dimensions=True, output=save_loc)

