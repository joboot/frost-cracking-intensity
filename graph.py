import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import constant


def main():
    print("graph main")


def create_graph(dataframe):
    """

    :param dataframe:
    :return None:
    """
    max_x_value = np.max(dataframe.values) + .5
    max_y_value = dataframe.index[-1]

    graph = sns.scatterplot(data=dataframe, x=dataframe.values, y=dataframe.index, color='black', marker='o')

    graph.axis([0, max_x_value, 0, max_y_value])
    x_axis_label = "Frost Cracking Intensity (" + constant.fci_unit + ") 0 to -15 " + constant.degree_symbol + "C"
    graph.set_xlabel(xlabel=x_axis_label)
    graph.set_ylabel("Depth (cm)")
    graph.minorticks_on()

    ax = plt.gca()
    ax.set_ylim(ax.get_ylim()[::-1])
    ax.xaxis.set_ticks(np.arange(0, max_x_value, 1))
    ax.xaxis.tick_top()  # and move the X-Axis

    ax.yaxis.set_ticks(np.arange(0, max_y_value + 1, max_y_value/20))  # set y-ticks
    ax.yaxis.tick_left()  # remove right y-Ticks


def show_graph():
    """
    Displays currently created plot
    :return None:
    """
    plt.show()


if __name__ == "__main__":
    main()
