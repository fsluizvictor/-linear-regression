from src import config
from src.adapter import csv_utils, plot_utils


def plot_dataset_1():
    data = csv_utils.open_file_csv(config.DATASET_1_PATH)
    population = list()
    gain = list()
    for row in data:
        population.append(row[0])
        gain.append(row[1])
    plot_utils.plot(gain, population, plot_utils.GraphicProperties.GREEN_CIRCLE_MARKS)


def get_dataset_1():
    return csv_utils.open_file_csv(config.DATASET_1_PATH)


if __name__ == '__main__':
    plot_dataset_1()
