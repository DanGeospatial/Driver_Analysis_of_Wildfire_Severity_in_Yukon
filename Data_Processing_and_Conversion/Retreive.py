"""
Get all the datasets for each fire. Put the results in a folder as csv.
"""
from Data_Retreival.Topographic import getAspect, getElevation, getSlope, getTWI, getTPI
from Data_Retreival.Fire_danger_indices_ERA5 import getERA5L, getClimate
from Data_Retreival.Fire_Severity import getdNBR, getmNBR, getpre
from Data_Retreival.Land_Cover import getLC
from Data_Processing_and_Conversion.Scaler import resample_cubic

fires = ['81', '326', '162', '109', '83', '228', '113', '227', '157', '115', '64', '174', '170', '233', '243', '58',
         '134', '155', '178', '161', '119', '23', '266', '99', '242', '160', '31', '240', '139', '334', '296', '179',
         '95', '71', '313', '84', '248', '100', '232', '120', '171', '172', '77', '74', '177', '166', '259', '117',
         '239', '82', '199', '167', '148', '152', '142', '298', '66', '249', '131', '87', '260', '146', '230', '268',
         '329', '15', '129', '28', '321', '333']
fire_year = ['1995', '2019', '2004', '1998', '1995', '2009', '1998', '2009', '2004', '1998', '1994', '2004', '2004',
             '2009', '2010', '1994', '1999', '2004', '2004', '2004', '1999', '1990', '2013', '1996', '2010', '2004',
             '1991', '2009', '2001', '2019', '2015', '2004', '1995', '1994', '2017', '1995', '2011', '1996', '2009',
             '1999', '2004', '2004', '1994', '1994', '2004', '2004', '2013', '1998', '2009', '1995', '2006', '2004',
             '2003', '2004', '2002', '2015', '1994', '2011', '1999', '1995', '2013', '2003', '2009', '2013', '2019',
             '1989', '1999', '1990', '2018', '2019']

polygons = "D:/Research/Masters/5_Extracted/dNBR/Polygons/"
climate_loc = "I:/Wildfire_Climate_Export_v2/"
export_path = "I:/Wildfire_Extracted_v2/"


# Only turn this on if you want to extract new climate data
# Right now it is set to fire season
do_climate = False
if do_climate:
    # Remove duplicate years to speed up processing
    years_trim = list(set(fire_year))
    for year in years_trim:
        getERA5L(year)
        image = climate_loc + year + ".tiff"
        resample_cubic(image)

# !WARNING!
# !All files must be PERFECTLY aligned before using the remainder of this tool!
# You can use something like: https://www.arcgis.com/home/item.html?id=4f5e9d4e3b974890991d33e7e5251231

# Get all files and place them in the correct directories
for fire in fires:
    fire_box = polygons + fire + "/" + fire + ".shp"
    save_loc = export_path + fire + "/" + fire
    fire_index = fires.index(fire)
    year_of_fire = fire_year[fire_index]

    getdNBR(fire_box, fire, save_loc)
    getmNBR(fire_box, save_loc)
    getAspect(fire_box, save_loc)
    getTPI(fire_box, save_loc)
    getTWI(fire_box, save_loc)
    getSlope(fire_box, save_loc)
    getElevation(fire_box, save_loc)
    getLC(fire_box, save_loc)
    getpre(fire_box, year_of_fire, save_loc)
    # Check getClimate function to choose which average period is extracted
    getClimate(fire_box, year_of_fire, save_loc)

