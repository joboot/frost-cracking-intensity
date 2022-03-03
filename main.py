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
from collections import deque
import numpy as np
from numpy import array
import pandas as pd
import matplotlib.pyplot as plt

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.6.2021"
__status__ = "Development"


def main():
    # mean_annual_temp, max_summer_temp, min_winter_temp, delta_depth, temp_over_depth = inputs()
    global array
    day_list = []
    change_in_depth = []

    depths = []
    for i in range(0, 2010, 10):
        depths.append(i)

    days = []
    for i in range(1, 366):
        days.append(i)

    mean_annual_temp = 0.1
    max_summer_temp = 10.9
    min_winter_temp = -10.9
    delta_depth = 10
    temp_over_depth = 0
    depth = 0
    day = 1

    while depth <= 2000:

        while day <= 365:
            # temp = calculations(mean_annual_temp, max_summer_temp, min_winter_temp, depth, day)
            temp = round(calculations(mean_annual_temp, max_summer_temp, min_winter_temp, depth, day), 2)

            day += 1
            day_list.append(temp)

            """
            if  0 >= change_in_day[day - 1] <= -15:
                math.fabs()
            """
        array = np.array_split(np.append(change_in_depth, day_list, axis=0), 201)

        change_in_depth.extend(day_list)

        day_list.clear()

        day = 1
        depth = depth + delta_depth

    final_dataframe = pd.DataFrame(array, index=depths, columns=days)
    print(final_dataframe)


def inputs():
    mean_annual_temp = float(input('Enter mean annual temperature(MAT): '))
    max_summer_temp = float(input('Enter maximum summer temperature(sT): '))
    min_winter_temp = float(input('Enter minimum winter temperature(wT): '))
    delta_depth = float(input('Enter change in depth(delta z): '))
    temp_over_depth = float(input('Enter change in temperature over change in depth(dT/dz): '))

    return mean_annual_temp, max_summer_temp, min_winter_temp, delta_depth, temp_over_depth


def calculations(mean_annual_temp, max_summer_temp, min_winter_temp, depth, day):
    alpha = 1296
    pi = math.pi
    year_period = 365

    # Ta = Half of the difference between max summer and winter min temps
    Ta = (max_summer_temp - min_winter_temp) / 2

    # frost cracking equation
    temp = mean_annual_temp + (Ta * math.exp(-depth * (pi / (alpha * year_period)) ** 0.5)) * math.sin(
        ((2 * pi * day) / year_period) - depth * ((pi / (alpha * year_period)) ** 0.5))

    return temp


def check_temp(temps):
    print("check temps")


def output():
    print('Output: ')


if __name__ == "__main__":
    main()
