import numpy as np
import os
import cv2
import os, random, shutil
path = 'C:/Users/Lab722-2080/image_inpainting/25_celeba/datasets/place2_256/'
files = os.listdir(path)

def put_mask(img_path,output_fold):
    image = cv2.imread(img_path)
    mask =cv2.imread('C:/Users/Lab722-2080/image_inpainting/25_celeba/datasets/place2_256/mask_dataset/mask00000001.jpg')

    try:
        alpha = 1
        beta = 1
        gamma = 0
        mask_img = cv2.addWeighted(image, alpha, mask, beta, gamma)
        cv2.imwrite(os.path.join(output_fold,'0000000012.jpg'), mask_img)
    except:
        print('error')

n = 0
gg = 251
ggg = 3765
for ii in range(15):
    for i in range(gg):
        z = str(n + 1).zfill(8)
        put_mask(img_path = 'C:/Users/Lab722-2080/image_inpainting/25_celeba/datasets/place2_256/000000001.jpg',
                 output_fold='C:/Users/Lab722-2080/image_inpainting/25_celeba/datasets/place2_256/')
        n = n + 1
print("finish_all")

