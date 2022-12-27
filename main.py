import torch
from roboflow import Roboflow
import wget
import train
import matplotlib.pyplot as plt
import glob
from IPython.display import Image, display
import cv2
import glob
import os


def prepere_ds():
    rf = Roboflow(api_key="ElP863CGwDANvcSPEIHJ")
    # project = rf.workspace("computer-vision-in-medicine-ex1").project("computer-vision-ex1")
    # dataset = project.version(3).download("yolov7")
    url = 'https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt'
    filename = wget.download(url)
    # return dataset.location


def text_update(frame, left_labels_list, right_labels_list):
    left_label = ''
    right_label = ''
    for interval in left_labels_list:
        if interval["start"] <= frame <= interval["stop"]:
            left_label = interval["class"]
            break
    for interval in right_labels_list:
        if interval["start"] <= frame <= interval["stop"]:
            right_label = interval["class"]
            break
    return f'Ground Truth: L- {left_label} | R-{right_label}'


def dynamic_labels():
    tool_usage = {"T0": "no tool in hand",
                  "T1": "needle_driver",
                  "T2": "forceps",
                  "T3": "scissors"}
    for video in glob.glob("/home/roi/PycharmProjects/yolov7/computer-vision-ex1-3/videos/P023_tissue2.wmv"):

        text_labels = str(os.path.basename(video)[:-4]) + ".txt"
        left_labels_list = list(open("computer-vision-ex1-3/tool_usage/tools_left/" + text_labels))
        right_labels_list = list(open("computer-vision-ex1-3/tool_usage/tools_right/" + text_labels))
        left_labels_list = [l.split() for l in left_labels_list]
        right_labels_list = [l.split() for l in right_labels_list]
        left_labels_list = [{"start": int(l[0]), "stop": int(l[1]), "class": "class " + tool_usage[l[2]]} for l in
                            left_labels_list]
        right_labels_list = [{"start": int(l[0]), "stop": int(l[1]), "class": "class " + tool_usage[l[2]]} for l in
                             right_labels_list]
        frame_ = 0
        loaded_video = cv2.VideoCapture(video)
        frame_width = int(loaded_video.get(3))
        frame_height = int(loaded_video.get(4))
        size = (frame_width, frame_height)

        out = cv2.VideoWriter(video[:-4] + ".mp4", cv2.VideoWriter_fourcc(*'MJPG'),
                              40, size)
        while (loaded_video.isOpened()):
            ret, frame = loaded_video.read()
            font = cv2.FONT_HERSHEY_SIMPLEX

            on_video_text = text_update(frame_, left_labels_list, right_labels_list)
            cv2.putText(frame, on_video_text, (50, 50), font, 0.5, (0, 255, 255), 2, cv2.LINE_4)

            # write the flipped frame
            out.write(frame)

            frame_ = frame_ + 1
            try:
                cv2.imshow(str(os.path.basename(video[:-4])), frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            except:
                print("lalala")

        loaded_video.release()
        out.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    dynamic_labels()
    print(torch.cuda.is_available())

    # /home/roi/PycharmProjects/yolov7/computer-vision-ex1-3
