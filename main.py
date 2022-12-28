import torch
from roboflow import Roboflow
import wget
import train

def prepere_ds():
    rf = Roboflow(api_key="ElP863CGwDANvcSPEIHJ")
    project = rf.workspace("computer-vision-in-medicine-ex1").project("computer-vision-ex1")
    dataset = project.version(3).download("yolov7")
    print(dataset.location)
    url = 'https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt'
    filename = wget.download(url)
    # return dataset.location

if __name__ == '__main__':
    prepere_ds()
    print(torch.cuda.is_available())

    #/home/roi/PycharmProjects/yolov7/computer-vision-ex1-3
