"""
Remove features to improve accuracy and efficiency by dropping features that are add error, etc.
"""
import pandas as pd
from os import scandir

input_path = "I:/Wildfire_Compiled_v2/"
datasets_path = "I:/Wildfire_Datasets_v2/combined.csv"
clean_path = "I:/Wildfire_Datasets_v2/combined_clean.csv"
checked_path = "I:/Wildfire_Datasets_v2/combined_check.csv"
combined_ds = []

# Merge all the csv files into one
with scandir(input_path) as pth:
    for file in pth:
        ds = pd.read_csv(file)
        combined_ds.append(ds)
df = pd.concat(combined_ds)
df.to_csv(datasets_path)

# Print column headers
print(df.columns)

# Remove variables that are known to have errors
error_columns = ['Unnamed: 0', 'x', 'y', 'spatial_ref', '49_clm', '50_clm', 'clm']
df.drop(error_columns, axis=1, inplace=True)

# Drop irrelevant features, i.e. lake temperature
irrelevant_columns = ['8_clm', '9_clm', '10_clm', '11_clm', '12_clm', '13_clm', '14_clm', '15_clm', '16_clm', '17_clm',
                      '18_clm', '19_clm', '20_clm', '21_clm', '22_clm', '41_clm']
df.drop(irrelevant_columns, axis=1, inplace=True)

# Remove no data rows
df = df[df.LC != -128]

# Remove unburned rows
df = df[df.dNBR < -100]
df.to_csv(clean_path)

# Print remaining columns and rows
print(df.columns)
print(df.shape)
print(df.eq(0).sum().sum())
print(df.isnull().sum().sum())

# Double Check Input Data
# This part is not needed I check the data in another software
# df = df[df.dNBR != -340282300000000000000000000000000000000.00]
# df.to_csv(checked_path)
df.boxplot(column=['dNBR', 'Slope', '2_clm'])
