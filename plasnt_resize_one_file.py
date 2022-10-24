import csv, os, time
import numpy as np
import cv2

path = 'E:/checked_imagefile/betel/'
crop_path = 'E:/AIcup_plant_33_autumn_croped/betel/'

path_list = os.listdir(path)
# print(path_list)

for n in path_list:
    img = cv2.imread(path + n)
    crop_img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
    cv2.imwrite(crop_path+n, crop_img)

