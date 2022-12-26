from glob import glob
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter


def extract_files_labels(file_path):
    labels = []
    with open(file_path) as f:
        lines = f.readlines()
        for l in lines:
            label = l.split(' ')[0]
            labels.append(label)

    return labels


def calc_class_balance(ds_labels_path, graph_title):
    ds_labels_files = glob(f'{ds_labels_path}/**')
    ds_labels_per_file = [extract_files_labels(file) for file in ds_labels_files]
    complete_labels = []
    for label_pair in ds_labels_per_file:
        complete_labels += label_pair

    # complete_labels = [int(x) for x in complete_labels]
    class_names = ['Right\nScissors',
                   'Left\nScissors',
                   'Right\nNeedle\ndriver',
                   'Left\nNeedle\ndriver',
                   'Right\nForceps',
                   'Left\nForceps',
                   'Right\nEmpty',
                   'Left\nEmpty']

    # Set the values to be plotted

    # Create the histogram
    plt.hist(complete_labels)

    # add title
    plt.title(graph_title)

    # Set the labels for the x-axis tick marks
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7], class_names)

    # Show the plot
    plt.show()

    plt.hist(complete_labels, weights=np.ones(len(complete_labels)) / len(complete_labels))

    plt.title(f'percentages {graph_title}')

    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7], class_names)
    plt.show()



if __name__ == '__main__':
    general_ds_path = '/home/tomer/PycharmProjects/yolov7/raw_data_ex1'
    for set_type in ('train', 'validation', 'test'):
        set_ds_path = f'{general_ds_path}/{set_type}/bboxes_labels'
        calc_class_balance(set_ds_path, f'{set_type} class count')
        exit()
