import numpy as np
import math
from numpy import genfromtxt
def windArray_u(direction, speed):
    i = 0
    numReadings = 150
    numSubThousand = 50
    step = 1000/numSubThousand
    windArrayU = np.zeros((numReadings, 2))
    radians = (((360-direction)-90)*math.pi)/180
    while i*step <= 1000 :
        if i == 0:
            windArrayU[0,0] = 10
            windArrayU[0,1] = speed*(math.cos(radians))
            i+=1
        else:
            windArrayU[i, 0] = i*step
            windArrayU[i, 1] = windArrayU[0,1]*pow((i*step)/10, .2)
            i+=1
        if abs(windArrayU[i-1, 1]) < 1.0 * pow(10,-6):
            windArrayU[i-1, 1] = 0
        print(f"The wind speed at altitude {windArrayU[i-1,0]}m is {windArrayU[i-1,1]}m/s East")

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