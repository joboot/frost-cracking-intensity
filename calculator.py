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

import GUI
import readWrite
import graph

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.6.2021"
__status__ = "Development"


def main():
    # mean_annual_temp, max_summer_temp, min_winter_temp, delta_depth = inputs()

    # For testing purposes
    mean_annual_temp = 0.1
    max_summer_temp = 10.9
    min_winter_temp = -10.9
    max_depth = 2000
    delta_depth = 10

    # Main loop to get the data required
    data_list, depths, days = loop(max_depth, delta_depth, mean_annual_temp, max_summer_temp, min_winter_temp)

    # Create dataframes out of the data
    ta_dataframe, ccm_dataframe, fci_dataframe, total_fci = \
        create_dataframes(data_list, max_depth, delta_depth, depths, days)

    # Displays dataframes and total FCI
    display_output(ta_dataframe, ccm_dataframe, fci_dataframe, total_fci)

    # print(ta_dataframe.head)

    GUI.calculate_fci()
    # graph.plot_data(fci_dataframe)
    # readWrite.main()


def inputs():
    # Mean annual temperature
    mean_annual_temp = float(input('Enter mean annual temperature(MAT): '))
    # Maximum summer temperature
    max_summer_temp = float(input('Enter maximum summer temperature(sT): '))
    # Minimum winter temperature
    min_winter_temp = float(input('Enter minimum winter temperature(wT): '))
    # The intervals in which depth changes
    delta_depth = float(input('Enter change in depth(delta z): '))

    return mean_annual_temp, max_summer_temp, min_winter_temp, delta_depth


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


def create_dataframes(data_list, max_depth, delta_depth, depths, days):
    # Creation of a 2D numpy array using the split function to split the entirety data into different rows based
    # on the maximum depth and each depth interval
    tz_array = np.array_split(data_list, (max_depth / delta_depth) + 1)

    # Create dataframe for the T/z (Temperature over depth)
    ta_dataframe = pd.DataFrame(tz_array, index=depths, columns=days)

    # Create a numpy array from the initial data list
    ccm_array = np.array(data_list)

    # Variable for the index of the current element
    index = 0

    # np.nditer function to iterate through the numpy array
    # Uses the optional flag 'readwrite' to change the array based on a if/else statement
    for i in np.nditer(ccm_array, op_flags=['readwrite']):
        # If the temperatures are between 0 and -15
        if 0 >= i >= -15:
            # Variable for the the next depth on the same day
            j = ccm_array[index + 365]
            # Celsius/centimeter equation
            i[...] = math.fabs((j - i)/delta_depth)
        else:
            # If not between 0 and -15, make it 0
            i[...] = 0

        # Increment index
        index += 1

    # Split the array into years at certain depths
    ccm_array = np.array_split(ccm_array, (max_depth / delta_depth) + 1)
    # Create Celsius/centimeter dataframe based on that array
    ccm_dataframe = pd.DataFrame(ccm_array, index=depths, columns=days)

    # Dataframe of the FCI at each depth
    fci_dataframe = ccm_dataframe["FCI"] = ccm_dataframe.sum(axis=1)

    # Total FCI for the entire year at all depths
    total_fci = fci_dataframe.sum(axis=0)

    return ta_dataframe, ccm_dataframe, fci_dataframe, total_fci


def display_output(ta_dataframe, ccm_dataframe, fci_dataframe, total_fci):
    # Display array while rounding to 2 decimal places
    print(ta_dataframe.round(2))

    # Display array while rounding to 2 decimal places
    print(ccm_dataframe.round(2))

    # Display array while rounding to 2 decimal places
    print(fci_dataframe.round(2))

    print()
    print("Total FCI:", round(total_fci))


def loop(max_depth, delta_depth, mean_annual_temp, max_summer_temp, min_winter_temp):

    depth = 0
    day = 1

    # 1D list holding data for each day at each depth
    data_list = []

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
            temp = calculations(mean_annual_temp, max_summer_temp, min_winter_temp, depth, day)

            # Add new calculation to the list of data
            data_list.append(temp)

            day += 1

        # Set the day back to 1 for the next depth
        day = 1

        # Change the depth to the next depth based on the depth interval
        depth = depth + delta_depth

    return data_list, depths, days


if __name__ == "__main__":
    main()
