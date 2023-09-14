import math
import numpy as np
import pandas as pd
import graph

__author__ = "Jordan Booth"
__version__ = "1.0"
__date__ = "10.6.2021"
__status__ = "Development"


def main():
    # For testing purposes
    mean_annual_temp = -14
    max_summer_temp = 38
    min_winter_temp = -68
    max_depth = 5000
    delta_depth = 10
    thermal_diffusivity = 1296
    window_max = 0
    window_min = -15

    # testing depth intervals with dataframe errors
    # test_depth_interval()

    # testing graph function
    test_graph(mean_annual_temp, max_summer_temp, min_winter_temp, max_depth, thermal_diffusivity,
               window_max, window_min, delta_depth)


def calculate_fci(entries):
    """
    Calculates and returns FCI and corresponding dataframes for user viewing
    :param entries: List of all parameters required to calculate fci defined by the user input
    :returns round(total_fci): Rounded total FCI for the year
             fci_dataframe: Dataframe containing the FCI at all depths
             depth_to_0: The depth at which FCI reaches 0 cm
             round(total_fci_fci_10015): Standardized rounded total FCI for the year
                                         (10 cm depth interval, 0--15 degrees C frost cracking window)
             fci_dataframe_fci_10015: Dataframe containing the standardized FCI at all depths
                                      (10 cm depth interval, 0--15 degrees C frost cracking window)
             depth_to_0_fci_10015: The depth at which FCI reaches 0 cm
                                   (10 cm depth interval, 0--15 degrees C frost cracking window)
    """
    if None in entries:
        return None

    mean_annual_temp, max_summer_temp, min_winter_temp, max_depth, delta_depth, thermal_diffusivity, \
        window_max, window_min = entries

    if window_min >= window_max:
        return None

    full_data_list, data_list, depths, days = \
        run_calculations(mean_annual_temp, max_summer_temp, min_winter_temp, max_depth, delta_depth, thermal_diffusivity)
    full_data_list_fci_10015, data_list_fci_10015, depths_fci_10015, days_fci_10015 = \
        run_calculations(mean_annual_temp, max_summer_temp, min_winter_temp, max_depth, 10, thermal_diffusivity)

    # Creation of dataframes with user defined parameters
    ta_dataframe, ccm_dataframe, fci_dataframe, total_fci = \
        create_dataframes(full_data_list, data_list, max_depth, delta_depth, depths, days, window_max, window_min)

    # Creation of dataframes at standardized FCI 10015 (10cm depth interval, 0--15 degrees C frost cracking window)
    ta_dataframe_fci_10015, ccm_dataframe_fci_10015, fci_dataframe_fci_10015, total_fci_fci_10015 = \
        create_dataframes(full_data_list_fci_10015, data_list_fci_10015, max_depth, 10, depths_fci_10015,
                          days_fci_10015, 0, -15)

    fci_dataframe = fci_dataframe.round(2)
    fci_dataframe_fci_10015 = fci_dataframe_fci_10015.round(2)

    depth_to_0 = fci_dataframe[fci_dataframe == 0].first_valid_index()
    depth_to_0_fci_10015 = fci_dataframe_fci_10015[fci_dataframe_fci_10015 == 0].first_valid_index()

    # Displays dataframes and total FCI
    # display_output(ta_dataframe, ccm_dataframe, fci_dataframe, total_fci)

    return round(total_fci), fci_dataframe, depth_to_0, round(total_fci_fci_10015), fci_dataframe_fci_10015, \
           depth_to_0_fci_10015


def tz_calculation(mean_annual_temp, max_summer_temp, min_winter_temp, depth, day, thermal_diffusivity):
    """
    Calculation for temperature as a function of depth T(z,t)
    :param mean_annual_temp: Average temperature for the year
    :param max_summer_temp: Maximum summer temperature
    :param min_winter_temp: Minimum winter temperature
    :param depth: The depth at which FCI is being calculated
    :param day: The day of which FCI is being calculated
    :param thermal_diffusivity: The thermal diffusivity of rock
    :return temp: Temporary variable to hold the calculation
    """
    pi = math.pi
    year_period = 365

    # Ta = Half of the difference between max summer and winter min temps
    ta = (max_summer_temp - min_winter_temp) / 4

    # tz equation
    temp = mean_annual_temp + (ta * math.exp(-depth * (pi / (thermal_diffusivity * year_period)) ** 0.5)) * math.sin(
        ((2 * pi * day) / year_period) - depth * ((pi / (thermal_diffusivity * year_period)) ** 0.5))

    return temp


def create_dataframes(full_data_list, data_list, max_depth, delta_depth, depths, days, window_max, window_min):
    """
    Creation of pandas dataframes of the data lists and the data from the annual sum of the temperature gradient that
    occurs in the frost cracking window specified.
    :param full_data_list: Full list of data of the T(z,t) calculations
    :param data_list: Shortened list of data of the T(z,t) calculations
    :param max_depth: Maximum depth desired
    :param delta_depth: Depth interval desired
    :param depths: List of all depths at which FCI is calculated
    :param days: List of all days in which FCI is calculated
    :param window_max: Frost cracking window maximum temperature
    :param window_min: Frost cracking window minimum temperature
    :returns ta_dataframe: Dataframe holding the data for T(z,t)
             ccm_dataframe: Dataframe holding the data for the annual sum of the temperature gradient that
                    occurs in the frost cracking window specified
             fci_dataframe: Dataframe holding the data for FCI
             total_fci: Total frost cracking intensity for the year
    """
    split_data_list = []
    for i in range(0, len(data_list), 365):
        x = i
        split_data_list.append(data_list[x:x + 365])

    ta_dataframe = pd.DataFrame(split_data_list, index=depths, columns=days)

    full_ccm_array = np.array(full_data_list)
    # Create a numpy array from the initial data list
    ccm_array = np.array(data_list)

    # Variable for the index of the current element
    index = 0

    # np.nditer function to iterate through the numpy array
    # Uses the optional flag 'readwrite' to change the array based on a if/else statement
    for i in np.nditer(ccm_array, op_flags=['readwrite']):
        # If the temperatures are between 0 and -15
        if int(window_max) >= i >= int(window_min):
            # Variable for the the next depth on the same day

            j = full_ccm_array[index + 365]

            # Celsius/centimeter equation
            i[...] = math.fabs((j - i) / delta_depth)
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


def display_output(tz_dataframe, ccm_dataframe, fci_dataframe, total_fci):
    """
    Displays dataframes and final FCI for the year to the console.
    :param tz_dataframe:
    :param ccm_dataframe:
    :param fci_dataframe:
    :param total_fci:
    :returns None:
    """
    # Display arrays in console
    print(tz_dataframe.round(2))
    print(ccm_dataframe.round(2))
    print(fci_dataframe.round(2))
    print()
    print("Total FCI:", round(total_fci))


def run_calculations(mean_annual_temp, max_summer_temp, min_winter_temp, max_depth, delta_depth, thermal_diffusivity):
    """
    Creation of data by running through calculations for T(z,t)
    :param mean_annual_temp: Average temperature for the year
    :param max_summer_temp: Maximum summer temperature
    :param min_winter_temp: Minimum winter temperature
    :param max_depth: Maximum depth desired
    :param delta_depth: Depth interval desired
    :param thermal_diffusivity: The thermal diffusivity of rock
    :returns full_data_list: Full list of data of the T(z,t) calculations
             data_list: Shortened list of data of the T(z,t) calculations
             depths: All depths
             days: Days of the year
    """
    depth = 0
    day = 1

    # 1D list holding data for each day at each depth
    full_data_list = []

    # List to hold the depths for the indices
    depths = []
    # Creates a range between 0-max_depth (Maximum depth) with intervals of delta_depth (Change in depth)
    # for i in np.arange(0, max_depth + 1, delta_depth):
    for i in range(0, int(max_depth + 1), int(delta_depth)):
        depths.append(i)

    # List to hold the numbered days of the year for the columns
    days = []
    # Creates a range between 1-365 for each day of the year
    for i in range(1, 366):
        days.append(i)

    # Loop to get the date for all of depth intervals max depth and under
    while depth <= max_depth + delta_depth * 5:

        # Loop to get the calculations in a year at this depth interval
        while day <= 365:
            # Calculate T(z,t) Temperature as a function of depth in bedrock and time
            temp = tz_calculation(mean_annual_temp, max_summer_temp, min_winter_temp, depth, day, thermal_diffusivity)

            # Add new calculation to the list of data
            full_data_list.append(temp)

            day += 1

        # Set the day back to 1 for the next depth
        day = 1

        # Change the depth to the next depth based on the depth interval
        depth = depth + delta_depth

    data_list = full_data_list[: - int(5 * 365)]

    return full_data_list, data_list, depths, days


def test_depth_interval():
    """
    Tests and logs errors with depth intervals. Mainly used in testing of decimal numbers
    :returns None:
    """
    mean_annual_temp = .1
    max_summer_temp = 10
    min_winter_temp = -10
    max_depth = 2000
    thermal_diffusivity = 1296
    window_max = 0
    window_min = -15

    delta_depth = 1

    error_numbers = []
    num_errors = 0
    num_intervals_tested = 0
    while delta_depth < 50.1:
        # Main loop to get the data required
        try:
            num_intervals_tested += 1
            full_data_list, data_list, depths, days = run_calculations(mean_annual_temp, max_summer_temp, min_winter_temp,
                                                                       max_depth,
                                                                       delta_depth, thermal_diffusivity)

            # Create dataframes out of the data
            ta_dataframe, ccm_dataframe, fci_dataframe, total_fci = \
                create_dataframes(full_data_list, data_list, max_depth, delta_depth, depths, days, window_max,
                                  window_min)
        except ValueError:
            error_numbers.append(delta_depth)
            num_errors = num_errors + 1

        delta_depth = delta_depth + 1


def test_graph(mean_annual_temp, max_summer_temp, min_winter_temp, max_depth, thermal_diffusivity, window_max,
               window_min, delta_depth):
    """

    :param mean_annual_temp: TODO
    :param max_summer_temp: TODO
    :param min_winter_temp: TODO
    :param max_depth: TODO
    :param thermal_diffusivity: TODO
    :param window_max: TODO
    :param window_min: TODO
    :param delta_depth: TODO
    :returns None: TODO
    """
    full_data_list, data_list, depths, days = run_calculations(mean_annual_temp, max_summer_temp, min_winter_temp, max_depth,
                                                               delta_depth, thermal_diffusivity)

    ta_dataframe, ccm_dataframe, fci_dataframe, total_fci = \
        create_dataframes(full_data_list, data_list, max_depth, delta_depth, depths, days, window_max, window_min)

    graph.create_graph(fci_dataframe)
    graph.show_graph()


if __name__ == "__main__":
    main()
