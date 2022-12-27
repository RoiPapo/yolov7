from glob import glob
import shutil

def extract_files_labels(file_path):
    labels = []
    with open(file_path) as f:
        lines = f.readlines()
        for l in lines:
            label = l.split(' ')[0]
            labels.append(label)

    return labels


def over_sample_ds():
    percentage_statistics = {'7': 0.3189326556543837, '0': 0.1181702668360864, '2': 0.33799237611181704,
                             '3': 0.020330368487928845, '5': 0.16200762388818296, '6': 0.041296060991105464,
                             '1': 0.0012706480304955528}

    oversampled_train_path = '/home/tomer/PycharmProjects/yolov7/raw_data_ex1/oversampled_ds/train/'

    original_train_images = glob('/home/tomer/PycharmProjects/yolov7/raw_data_ex1/original_ds/train/images/*.jpg')
    original_train_bbx_plot = glob(
        '/home/tomer/PycharmProjects/yolov7/raw_data_ex1/original_ds/train/bboxes_labels/*.txt')

    for im_ads in original_train_images:
        img_file_name = im_ads.split('/')[-1].replace('.jpg', '')
        bbx_plot_name = im_ads.replace('jpg', 'txt').replace('images', 'bboxes_labels')
        if bbx_plot_name in original_train_bbx_plot:
            im_classes = extract_files_labels(bbx_plot_name)
            if '7' in im_classes or '2' in im_classes:
                shutil.copyfile(im_ads, f'{oversampled_train_path}/images/{img_file_name}.jpg')
                shutil.copyfile(bbx_plot_name, f'{oversampled_train_path}/bboxes_labels/{img_file_name}.txt')
            elif '1' in im_classes or '3' in im_classes or '6' in im_classes:
                for idx in range(35):
                    shutil.copyfile(im_ads, f'{oversampled_train_path}/images/{img_file_name}_{idx}.jpg')
                    shutil.copyfile(bbx_plot_name, f'{oversampled_train_path}/bboxes_labels/{img_file_name}_{idx}.txt')
            elif '0' in im_classes or '5' in im_classes:
                for idx in range(3):
                    shutil.copyfile(im_ads, f'{oversampled_train_path}/images/{img_file_name}_{idx}.jpg')
                    shutil.copyfile(bbx_plot_name, f'{oversampled_train_path}/bboxes_labels/{img_file_name}_{idx}.txt')


if __name__ == '__main__':
    over_sample_ds()
