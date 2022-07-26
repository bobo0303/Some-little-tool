import os

import cv2
import numpy as np
path = 'F:/mask_dataset/R/'

path1 = 'C:/Users/Lab722-2080/image_inpainting/25_celeba/mask/256/'
path2 = 'C:/Users/Lab722-2080/image_inpainting/25_celeba/mask/256_colorchange/'
number = os.listdir(path)
nn = len(number)

for n in range(nn):
    x = 8
    pad = '0'
    z = str(n).rjust(x, pad)
    # 灰度 0-255 255-當前灰度值
    img = cv2.imread(path + 'thin_strokes_'+z+'.png', 1)
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    dst = np.zeros((height, width, 1), np.uint8)

    for i in range(height):
        for j in range(width):
            grayPixel = 255 - gray[i, j]
            dst[i, j] = grayPixel

    cv2.imwrite(path + 'mask_'+z+'.png', dst)