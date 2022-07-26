import cv2, os
import numpy as np

path = 'F:/mask_dataset/R/'
path2 ='F:/mask_dataset/RR/'
file = os.listdir(path)
file_n = len(file)
list = []
x = 8
xWx = 0
pad = '0'
for n in file:
    image = cv2.imread(path+n, 0)
    kernel = np.ones((3,3), np.uint8)
    #erosion = cv2.erode(image, kernel, iterations = 1)
    dilation = cv2.dilate(image, kernel, iterations = 1)

    '''cv2.imshow('Input', image)
    cv2.imshow('Result', erosion)
    cv2.imshow('Result2', dilation)'''
    #cv2.imwrite(path+'Result_'+n,erosion)
    cv2.imwrite(path+'Result2_'+n,dilation)

    cv2.waitKey(0)