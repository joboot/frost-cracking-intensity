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
import numpy as np
import pandas as pd

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.6.2021"
__status__ = "Development"


def main():
    # mean_annual_temp, max_summer_temp, min_winter_temp, delta_depth, temp_over_depth = inputs()

    # 1D list holding data for each day at each depth
    data_list = []

    mean_annual_temp = 0.1
    max_summer_temp = 10.9
    min_winter_temp = -10.9
    max_depth = 2000
    delta_depth = 10
    temp_over_depth = 0
    depth = 0
    day = 1

    # List to hold the depths for the indices
    depths = []
    # Creates a range between 0-max_depth (Maximum depth) with intervals of delta_depth (Change in depth)
    for i in range(0, max_depth + 1, delta_depth):
        depths.append(i)

    # List to hold the numbered days of the year for the columns
    days = []
    # Creates a range between 1-365 for each day of the year
    for i in range(1, 366):
        days.append(i)

    # Loop to get the date for all of depth intervals 2000 cm and under
    while depth <= max_depth:

        # Loop to get the calculations in a year at this depth interval
        while day <= 365:
            # Calculate T(z,t) Temperature as a function of depth in bedrock and time
            # temp = calculations(mean_annual_temp, max_summer_temp, min_winter_temp, depth, day)
            temp = round(calculations(mean_annual_temp, max_summer_temp, min_winter_temp, depth, day), 2)

            # Add new calculation to the list of data
            data_list.append(temp)

            """
            if  0 >= change_in_day[day - 1] <= -15:
                math.fabs()
            """
            day += 1

        # Set the day back to 1 for the next depth
        day = 1

        # Change the depth to the next depth based on the depth interval
        depth = depth + delta_depth

    # Creation of a 2D numpy array using the split function to split the entirety data into different rows based
    # on the maximum depth and each depth interval
    tz_array = np.array_split(data_list, (max_depth / delta_depth) + 1)

    # Create dataframe for the T/z (Temperature over depth)
    ta_dataframe = pd.DataFrame(tz_array, index=depths, columns=days)
    print(ta_dataframe)

""" 
    test = np.array([-12, -30, -2, 5, 0, -2, -15]
                    [-24, 7, 81, 2, -6, -9, 10, -13])
    print(test)
    condlist = [test > 0, test < -15]
    choicelist = [0, 0]
    new_test = np.select(condlist, choicelist, test*10)
    print(new_test)

    #arr = np.arange(8)

    #print(arr)

    #condlist = [arr < 3, arr > 4]
    #choicelist = [arr, arr ** 3]

    #gfg = np.select(condlist, choicelist)

    #print(gfg)

"""


def inputs():
    # Mean annual temperature
    mean_annual_temp = float(input('Enter mean annual temperature(MAT): '))
    # Maximum summer temperature
    max_summer_temp = float(input('Enter maximum summer temperature(sT): '))
    # Minimum winter temperature
    min_winter_temp = float(input('Enter minimum winter temperature(wT): '))
    # The intervals in which depth changes
    delta_depth = float(input('Enter change in depth(delta z): '))

    temp_over_depth = float(input('Enter change in temperature over change in depth(dT/dz): '))

    return mean_annual_temp, max_summer_temp, min_winter_temp, delta_depth, temp_over_depth


def calculations(mean_annual_temp, max_summer_temp, min_winter_temp, depth, day):
    alpha = 1296
    pi = math.pi
    year_period = 365

    # Ta = Half of the difference between max summer and winter min temps
    ta = (max_summer_temp - min_winter_temp) / 2

    # frost cracking equation
    temp = mean_annual_temp + (ta * math.exp(-depth * (pi / (alpha * year_period)) ** 0.5)) * math.sin(
        ((2 * pi * day) / year_period) - depth * ((pi / (alpha * year_period)) ** 0.5))

    return temp


def check_temp(temps):
    print("check temps")


def output():
    print('Output: ')


if __name__ == "__main__":
    main()
