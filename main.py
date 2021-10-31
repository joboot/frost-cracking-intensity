"""
Program to calculate and determine frost cracking intensity
inputs:
MAT (mean annual Temperature)
max summer Temp
min winter Temp
z (depth)
change in z (change in depth)
dT/dz (change in temp over change in depth)
T should stay in between 0 - -15

outputs:
FCI (frost cracking intensity)
depth to 0 FCI
"""

import math

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.6.2021"
__status__ = "Development"

def main():
    
    mean_annual_temp, max_summer_temp, min_winter_temp, delta_depth, temp_over_depth = inputs()
    depth = 0
    day = 1
    change_in_day = []
    change_in_depth = []

    while depth <= 50:
        
        while day <= 5:
            change_in_day.clear
            print("day:", day)
            print("depth:", depth)
            temp = round(calculations(mean_annual_temp, max_summer_temp, min_winter_temp, depth, day), 2)
            day += 1
            change_in_day.append(temp)
            """
            if  0 >= change_in_day[day - 1] <= -15:
                math.fabs()
            """
        change_in_depth.append(change_in_day)
        day = 1
        depth = depth + delta_depth

    print(change_in_depth)

def inputs():

    mean_annual_temp = float(input('Enter mean annual temperature(MAT): '))
    max_summer_temp = float(input('Enter maximum summer temperature(sT): '))
    min_winter_temp = float(input('Enter minumum winter temperature(wT): '))
    delta_depth = float(input('Enter change in depth(delta z): '))
    temp_over_depth = float(input('Enter change in temperature over change in depth(dT/dz): '))

    return mean_annual_temp, max_summer_temp, min_winter_temp, delta_depth, temp_over_depth

def calculations(mean_annual_temp, max_summer_temp, min_winter_temp, depth, day):
    print('Calculating...')
    alpha = 1296
    pi = math.pi
    year_period = 365
    # Ta = Half of the difference between max summer and winter min temps
    Ta = (max_summer_temp - min_winter_temp)/2

    # frost cracking equation
    temp =  mean_annual_temp+((Ta*math.exp(-depth * (pi/(alpha*year_period))**0.5) ))* math.sin(((2*pi*day)/year_period) - depth * ((pi/(alpha*year_period))**0.5))
    print('T(z,t) =', str(temp))

    return temp

def check_temp(temps):
    print("check temps")

def output():
    print('Output: ')

if __name__ == "__main__":
    main()
