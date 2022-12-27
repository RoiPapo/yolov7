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

    percentage_statistics = {}
    for val in complete_labels:
        if val in percentage_statistics:
            percentage_statistics[val] += 1
        else:
            percentage_statistics[val] = 1

    for key in percentage_statistics:
        percentage_statistics[key] = percentage_statistics[key] / len(complete_labels)


    class_names = ['Right\nScissors',
                   'Left\nScissors',
                   'Right\nNeedle\ndriver',
                   'Left\nNeedle\ndriver',
                   'Right\nForceps',
                   'Left\nForceps',
                   'Right\nEmpty',
                   'Left\nEmpty']
    class_names_dict = {idx: x for idx, x in enumerate(class_names)}
    percentage_statistics_dict = {}
    for key, value in percentage_statistics.items():
        percentage_statistics_dict[class_names_dict[int(key)]] = value

    names = list(percentage_statistics_dict.keys())
    values = list(percentage_statistics_dict.values())

    plt.bar(range(len(percentage_statistics_dict)), values, tick_label=names)
    # plt.show()
    plt.savefig(fname=f'percentages: {graph_title}')
    plt.cla()
    plt.clf()


if __name__ == '__main__':
    general_ds_path = '/home/tomer/PycharmProjects/yolov7/raw_data_ex1/oversampled_ds'
    for set_type in ['train']: #('train', 'validation', 'test'):
        set_ds_path = f'{general_ds_path}/{set_type}/bboxes_labels'
        calc_class_balance(set_ds_path, set_type)
