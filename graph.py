import seaborn as sns
from matplotlib import pyplot as plt


def main():
    print("graph main")


def plot_data(dataframe):

    sns.lineplot(data=dataframe)
    # fci_graph.head()
    # print(plt.axis(1))
    plt.show()


if __name__ == "__main__":
    main()