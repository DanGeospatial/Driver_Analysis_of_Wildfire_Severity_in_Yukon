"""
Get all the datasets for each fire. Put the results in a folder as csv.
"""

from Data_Retreival.Topographic import getAspect
from Data_Retreival.Topographic import getElevation
from Data_Retreival.Topographic import getSlope
from Data_Retreival.Topographic import getTWI
from Data_Retreival.Topographic import getTPI
from Data_Retreival.Fire_danger_indices_ERA5 import getDanger
from Data_Retreival.Fire_Severity import getdNBR


fires = ['81', '326']

polygons = "D:/Research/Masters/5_Extracted/dNBR/Polygons/"
export_path = "I:/Wildfire_Extracted_v2/"

for fire in fires:
    fire_box = polygons + fire + "/" + fire + ".shp"
    save_loc = export_path + fire

    getdNBR(fire_box, fire, save_loc)
    getAspect(fire_box, save_loc)
