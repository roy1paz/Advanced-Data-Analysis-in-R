import pandas as pd
''' convert annual_aqi_by_county_2003-2020 table to a AQI group by year and state and save average values '''
full_aqi_df = pd.read_csv("C:\\Users\\roy1p\\PycharmProjects\\BGU python\\Advanced Programming project\RAW data\\annual_aqi_by_county_2003-2020\\annual_aqi_by_county_2003-2020.csv")
aqi_df_final = full_aqi_df.groupby(["Year",'State'])
aqi_df_final = aqi_df_final['Days with AQI', 'Good Days', 'Moderate Days', 'Unhealthy for Sensitive Groups Days',
                            'Unhealthy Days', 'Very Unhealthy Days', 'Hazardous Days', 'Max AQI', '90th Percentile AQI',
                            'Median AQI', 'Days CO', 'Days NO2', 'Days Ozone',
                            'Days SO2', 'Days PM2.5', 'Days PM10'].mean()

aqi_df_final.to_csv('aqi_by_State_2003-2020.csv')
