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

# ['81','326','162','109','83','228','113','227','157','115','64','174','170','233','243','58','134','155','178','161','119','23','266','99','242','160','31','240','139','334','296','179','95','71','313','84','248','100','232','120','171','172','77','74','177','166','259','117','239','82','199','167','148','152','142','298','66','249','131','87','260','146','230','268','329','15','129','28','321','333']
fires = ['81', '326']

polygons = "D:/Research/Masters/5_Extracted/dNBR/Polygons/"
export_path = "I:/Wildfire_Extracted_v2/"

for fire in fires:
    fire_box = polygons + fire + "/" + fire + ".shp"
    save_loc = export_path + fire

    getdNBR(fire_box, fire, save_loc)
    getAspect(fire_box, save_loc)
