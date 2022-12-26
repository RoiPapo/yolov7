from glob import glob
import matplotlib.pyplot as plt


def extract_files_labels(file_path):
    labels = []
    with open(file_path) as f:
        lines = f.readlines()
        for l in lines:
            label = l.split(' ')[0]
            labels.append(label)

    return labels


def calc_class_balance():
    ds_labels_path = '/home/tomer/PycharmProjects/yolov7/raw_data_ex1/HW1_dataset/bboxes_labels'
    ds_labels_files = glob(f'{ds_labels_path}/**')
    ds_labels_per_file = [extract_files_labels(file) for file in ds_labels_files]
    complete_labels = []
    for label_pair in ds_labels_per_file:
        complete_labels += label_pair

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

    # Set the labels for the x-axis tick marks
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7], class_names)

    # Show the plot
    plt.show()


if __name__ == '__main__':
    calc_class_balance()
