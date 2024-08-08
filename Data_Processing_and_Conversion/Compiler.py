"""
This will control creating the large wildfire dataset
"""
import xarray as xr
from os import scandir
from osgeo import gdal
import rasterio
import rioxarray

fires = ['81', '326', '162', '109', '83', '228', '113', '227', '157', '115', '64', '174', '170', '233', '243', '58',
         '134', '155', '178', '161', '119', '23', '266', '99', '242', '160', '31', '240', '139', '334', '296', '179',
         '95', '71', '313', '84', '248', '100', '232', '120', '171', '172', '77', '74', '177', '166', '259', '117',
         '239', '82', '199', '167', '148', '152', '142', '298', '66', '249', '131', '87', '260', '146', '230', '268',
         '329', '15', '129', '28', '321', '333']

import_path = "I:/Wildfire_Extracted_v2/"
output_path = "I:/Wildfire_Compiled_v2/"

print("Warning! If your files are not aligned PERFECTLY then this tool will not work properly!")
print(gdal.VersionInfo())

for fire in fires:
    input_dir = import_path + fire + "/"
    combined_ds = []

    with scandir(input_dir) as it:
        for file in it:
            if file.is_file():
                file_name = input_dir + file.name
                dr = rioxarray.open_rasterio(file_name, band_as_variable=True)
                remove_char = fire + "_"
                new_name = file.name.replace('.tif', '').replace(remove_char, '')
                name_dict = {'band_1': new_name}
                ds = dr.rename_vars(name_dict=name_dict)
                combined_ds.append(ds)

    file_out = output_path + fire + ".csv"
    output_ds = xr.merge(combined_ds)
    output_ds.to_dask_dataframe().to_csv(file_out, single_file=True)
