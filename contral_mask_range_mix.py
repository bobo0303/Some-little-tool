import os
import random
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


path = 'F:/mask_dataset/R/'
path2 ='F:/mask_dataset/RR/'
path3 ='F:/mask_dataset/RN/'

file = os.listdir(path)
file3 = os.listdir(path3)
file_n = len(file)
file_n2 = len(os.listdir(path2))
file_n3 = len(os.listdir(path3))
list = []

xWx = file_n2+1
kernel = np.ones((4, 4), np.uint8)
x1 = random.sample(file, len(file))
x2 = random.sample(file3, len(file3))

for n in range(file_n):
    for nn in range(file_n):

        rr1 = random.randint(0, 3)
        rr2 = random.randint(0, 3)
        ed1 = random.randint(0, 2)
        ed2 = random.randint(0, 2)
        bounes = random.randint(0, 5)

        if n == nn:
            continue

        view1 = cv2.imread(path+x1[n])
        view2 = cv2.imread(path+x1[nn])

        if rr1 == 0:
            view1 = cv2.rotate(view1, cv2.ROTATE_90_CLOCKWISE)
        elif rr1 == 1:
            view1 = cv2.rotate(view1, cv2.ROTATE_180)
        elif rr1 == 2:
            view1 = cv2.rotate(view1, cv2.ROTATE_90_COUNTERCLOCKWISE)
        if ed1 == 0:
            view1 = cv2.erode(view1, kernel, iterations = 1)
        if ed1 == 1:
            view1 = cv2.dilate(view1, kernel, iterations = 1)

        if rr2 == 0:
            view2 = cv2.rotate(view2, cv2.ROTATE_90_CLOCKWISE)
        elif rr2 == 1:
            view2 = cv2.rotate(view2, cv2.ROTATE_180)
        elif rr2 == 2:
            view2 = cv2.rotate(view2, cv2.ROTATE_90_COUNTERCLOCKWISE)
        if ed2 == 0:
            view2 = cv2.erode(view2, kernel, iterations = 1)
        if ed2 == 1:
            view2 = cv2.dilate(view2, kernel, iterations = 1)

        if bounes == 0:
            view3 = cv2.imread(path + x1[2])
            view1 = cv2.addWeighted(view1, 1, view3, 1, 0)

        z = str(xWx).zfill(8)

        view1 = cv2.addWeighted(view1, 1, view2, 1, 0)
        xWx+=1
        cv2.imwrite(path3+'xx6'+z+'.png', view1)
