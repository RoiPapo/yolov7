import torch
from roboflow import Roboflow


def prepere_ds():
    rf = Roboflow(api_key="ElP863CGwDANvcSPEIHJ")
    project = rf.workspace("computer-vision-in-medicine-ex1").project("computer-vision-ex1")
    dataset = project.version(3).download("yolov7")
    return dataset.location

if __name__ == '__main__':

    print(torch.cuda.is_available())
    #C:\Users\RoiPapo\PycharmProjects\yolov7\computer-vision-ex1-3
