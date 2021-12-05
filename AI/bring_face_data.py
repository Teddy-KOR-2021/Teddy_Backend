import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F
import os
from torch.autograd import Variable
import transforms as transforms
from skimage import io
from skimage.transform import resize
from models import *

os.environ['KMP_DUPLICATE_LIB_OK']='True'
class_names = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']


cut_size = 44
transform_test = transforms.Compose([
    transforms.TenCrop(cut_size),
    transforms.Lambda(lambda crops: torch.stack([transforms.ToTensor()(crop) for crop in crops])),
])

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


def recognizeFeeling(image):
    raw_img = io.imread(image)
    gray = rgb2gray(raw_img)
    gray = resize(gray, (48,48), mode='symmetric').astype(np.uint8)

    img = gray[:, :, np.newaxis]
    img = np.concatenate((img, img, img), axis=2)
    img = Image.fromarray(img)
    inputs = transform_test(img)

    net = VGG('VGG19')
    checkpoint = torch.load(os.path.join('FER2013_VGG19', 'PrivateTest_model.t7'), map_location=torch.device('cpu'))
    net.load_state_dict(checkpoint['net'])
    net.eval()

    ncrops, c, h, w = np.shape(inputs)
    with torch.no_grad():
        inputs = inputs.view(-1, c, h, w)
        # inputs = inputs.cuda()
        inputs = Variable(inputs)
        outputs = net(inputs)
        outputs_avg = outputs.view(ncrops, -1).mean(0)  # avg over crops
        score = F.softmax(outputs_avg, dim=0)
        return score.data.cpu().numpy()

# print(recognizeFeeling('images/1.jpg'))  체크