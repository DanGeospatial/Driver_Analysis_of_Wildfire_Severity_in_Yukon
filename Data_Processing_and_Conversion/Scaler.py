"""
Resample a raster to 30m
"""
import whitebox_tools

wbt = whitebox_tools.WhiteboxTools()
wbt.set_whitebox_dir("E:/Users/speed/anaconda3/envs/Yukon_Wildfire_Drivers_v2/Library/bin")
base = "D:/Research/Masters/3_Initial_Processing_Files/LandTrendR/LTR1_5/NBR_Fitted_2020.tif"


def resample_nearest(raster):
    output_name = raster + "_ rs" + ".tiff"

    wbt.resample(inputs=raster, output=output_name, base=base, method='nn')


def resample_cubic(raster):
    output_name = raster + "_ rs" + ".tiff"

    wbt.resample(inputs=raster, output=output_name, base=base, method='cc')
