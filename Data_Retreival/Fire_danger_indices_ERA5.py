import cdsapi
import ee
import geemap

url = "https://earthengine-highvolume.googleapis.com"
out_loc = "I:/Wildfire_Climate_Export_v2/"

# Initialize Earth Engine Api
# More information at developers.google.com/earth-engine/guides/python_install-conda#windows
ee.Initialize(url=url)
c = cdsapi.Client()


# This API is so slow it will take forever to download this way
# I have switched back to EE but EE only has ERA5 not Canadian FWI
def getFWIDanger(month, year, save_path):
    # Months should be listed as 'month': ['03', '04',]
    # Area should be BB extent
    c.retrieve(
        'cems-fire-historical-v1',
        {
            'format': 'grib',
            'grid': '0.25/0.25',
            'month': [month, ],
            'year': year,
            'system_version': '4_1',
            'dataset_type': 'consolidated_dataset',
            'variable': [
                'build_up_index', 'drought_code', 'duff_moisture_code',
                'fine_fuel_moisture_code', 'fire_daily_severity_rating', 'fire_weather_index',
                'initial_fire_spread_index',
            ],
            'product_type': 'reanalysis',
            'day': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
                '13', '14', '15',
                '16', '17', '18',
                '19', '20', '21',
                '22', '23', '24',
                '25', '26', '27',
                '28', '29', '30',
                '31',
            ],
            'area': [
                65, -143, 60,
                -130,
            ],
        },
        target=save_path + ".grib")


def getERA5L(year):
    boundary = ee.Image("users/danielnelsonca/Projects/Arctic_Ecozones_in_Canada")

    start_date = "'" + year + "-" + "05" + "'"
    end_date = "'" + year + "-" + "09" + "'"
    output = out_loc + year + ".tiff"

    dataset = (ee.ImageCollection("ECMWF/ERA5_LAND/MONTHLY_AGGR")
               .filter(ee.Filter.date(start_date, end_date))
               .filterBounds(boundary))

    average = dataset.reduce(ee.Reducer.mean()).clip(boundary)

    geemap.ee_to_geotiff(ee_object=average, output=output, resolution=11132)
