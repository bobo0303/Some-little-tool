import os

import cv2
import numpy as np
from matplotlib import pyplot as plt

path = 'F:/mask_dataset/strokes/'
path2 = 'F:/mask_dataset/RR/'
file = os.listdir(path)
name = 'thin_strokes_'
x = 8
xx = 0
pad = '0'

for n in file:
    file2 = os.listdir(path+n)
    print(n)
    for nn in file2:
        #print(nn)
        z = str(xx).rjust(x, pad)
        img = cv2.imread(path+n+'/'+nn, 0)
        r,th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
        cv2.imwrite(path+n+'/'+nn, th1)
        #print(path+name+z+'.png')
        xx+=1

