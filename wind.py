# Calculates wind based on wind at 10m and NOAA Sounding Data
from datetime import datetime
import numpy as np
import math
from numpy import genfromtxt

import FlightParams
import openmeteo_requests
import requests_cache
from retry_requests import retry


def makeWind(hour):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    url = "https://api.open-meteo.com/v1/forecast"

    now = datetime.now()
    current_date = now.date()  
    current_date = str(current_date)

    params = {
        "latitude": FlightParams.latitude,
        "longitude": FlightParams.longitude,
        "hourly": ["temperature_2m", "temperature_925hPa", "temperature_850hPa", "temperature_700hPa", "wind_speed_10m", "wind_speed_100m", "wind_speed_925hPa", "wind_speed_850hPa", "wind_speed_700hPa", "wind_direction_10m",  "wind_direction_100m", "wind_direction_925hPa", "wind_direction_850hPa", "wind_direction_700hPa"],
        "models": "ecmwf_ifs025",
        "timezone": "America/Chicago",
        "start_date": "2025-06-11",
        "end_date": "2025-06-11"
    }

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    hourly = response.Hourly()

    temperature_2m = hourly.Variables(0).ValuesAsNumpy()[hour]
    temperature_925hPa = hourly.Variables(1).ValuesAsNumpy()[hour]
    temperature_850hPa = hourly.Variables(2).ValuesAsNumpy()[hour]
    temperature_700hPa = hourly.Variables(3).ValuesAsNumpy()[hour]
    wind_speed_10m = hourly.Variables(4).ValuesAsNumpy()[hour] / 3600 * 1000
    wind_speed_100m = hourly.Variables(5).ValuesAsNumpy()[hour] / 3600 * 1000
    wind_speed_925hPa = hourly.Variables(6).ValuesAsNumpy()[hour] / 3600 * 1000
    wind_speed_850hPa = hourly.Variables(7).ValuesAsNumpy()[hour] / 3600 * 1000
    wind_speed_700hPa = hourly.Variables(8).ValuesAsNumpy()[hour] / 3600 * 1000
    wind_direction_10m = hourly.Variables(9).ValuesAsNumpy()[hour]
    wind_direction_100m = hourly.Variables(10).ValuesAsNumpy()[hour]
    wind_direction_925hPa = hourly.Variables(11).ValuesAsNumpy()[hour]
    wind_direction_850hPa = hourly.Variables(12).ValuesAsNumpy()[hour]
    wind_direction_700hPa = hourly.Variables(13).ValuesAsNumpy()[hour]
    
    wind_u = [[10, wind_speed_10m * math.cos((((360-wind_direction_10m)-90)*math.pi)/180)], 
              [100, wind_speed_100m * math.cos((((360-wind_direction_100m)-90)*math.pi)/180)], 
              [800, wind_speed_925hPa * math.cos((((360-wind_direction_925hPa)-90)*math.pi)/180)], 
              [1500, wind_speed_850hPa * math.cos((((360-wind_direction_850hPa)-90)*math.pi)/180)], 
              [3000, wind_speed_700hPa * math.cos((((360-wind_direction_700hPa)-90)*math.pi)/180)]]
    wind_v = [[10, wind_speed_10m * math.sin((((360-wind_direction_10m)-90)*math.pi)/180)], 
              [100, wind_speed_100m * math.sin((((360-wind_direction_100m)-90)*math.pi)/180)], 
              [800, wind_speed_925hPa * math.sin((((360-wind_direction_925hPa)-90)*math.pi)/180)], 
              [1500, wind_speed_850hPa * math.sin((((360-wind_direction_850hPa)-90)*math.pi)/180)], 
              [3000, wind_speed_700hPa * math.sin((((360-wind_direction_700hPa)-90)*math.pi)/180)]]



    return {"u": wind_u, "v": wind_v}



def windArray_u(direction, speed):
    i = 0
    numReadings = 150 # Total num of wind changes
    numSubThousand = 50 # Number of wind changes below 1000ft (calculated using power law)
    step = 1000/numSubThousand
    windArrayU = np.zeros((numReadings, 2))
    radians = (((360-direction)-90)*math.pi)/180 # Calculates radians given wind direction in degrees (wind direction is given in compass degrees)
    # Calculates first 1000m using power law 
    while i*step <= 1000 :
        if i == 0: # First measurement
            windArrayU[0,0] = 10
            windArrayU[0,1] = speed*(math.cos(radians))
            i+=1
        else: # Other sub thousand measurements
            windArrayU[i, 0] = i*step
            windArrayU[i, 1] = windArrayU[0,1]*pow((i*step)/10, .2)
            i+=1
        if abs(windArrayU[i-1, 1]) < 1.0 * pow(10,-6):
            windArrayU[i-1, 1] = 0
        print(f"The wind speed at altitude {windArrayU[i-1,0]}m is {windArrayU[i-1,1]}m/s East")

    # Reads data from csv file and calculates wind in the East direction
    weather_data = genfromtxt('WeatherData.csv', delimiter=',')
    row=0
    while weather_data[row,1] <= 4000.00:
        if weather_data[row, 4] != -9999.00 and weather_data[row,1] >= 1000:
            windArrayU[i, 0] = weather_data[row, 1]
            radians = (((360-weather_data[row,4])-90)*math.pi)/180
            windArrayU[i, 1] = weather_data[row,5]*(math.cos(radians))
            print(f"The wind speed at altitude {windArrayU[i,0]}m is {windArrayU[i,1]}m/s East")
            i+=1
        row+=1
    return windArrayU

def windArray_v(direction, speed):
    i = 0
    numReadings = 150
    numSubThousand = 50
    step = 1000/numSubThousand
    windArrayV = np.zeros((numReadings, 2))
    radians = (((360-direction)-90)*math.pi)/180
    while i*step <= 1000 :
        if i == 0:
            windArrayV[0,0] = 10
            windArrayV[0,1] = speed*(math.sin(radians))
            i+=1
        else:
            windArrayV[i, 0] = i*step
            windArrayV[i, 1] = windArrayV[0,1]*pow((i*step)/10, .2)
            i+=1
        if abs(windArrayV[i-1, 1]) < 1.0 * pow(10,-6):
            windArrayV[i-1, 1] = 0
        print(f"The wind speed at altitude {windArrayV[i-1,0]}m is {windArrayV[i-1,1]}m/s North")

    # Reads data from csv file and calculates wind in the North direction
    weather_data = genfromtxt('WeatherData.csv', delimiter=',')
    row=0
    while weather_data[row,1] <= 4000.00:
        if weather_data[row, 4] != -9999.00 and weather_data[row,1] >= 1000:
            windArrayV[i, 0] = weather_data[row, 1]
            radians = (((360-weather_data[row,4])-90)*math.pi)/180
            windArrayV[i, 1] = weather_data[row,5]*(math.sin(radians))
            print(f"The wind speed at altitude {windArrayV[i,0]}m is {windArrayV[i,1]}m/s North")
            i+=1
        row+=1
    return windArrayV