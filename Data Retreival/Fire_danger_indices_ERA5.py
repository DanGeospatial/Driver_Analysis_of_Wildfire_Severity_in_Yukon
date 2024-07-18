import cdsapi


c = cdsapi.Client()


def getDanger(month, year, area, savepath):
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
            'area': [area, ],
        },
        target=savepath)



