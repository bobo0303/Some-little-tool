# -*- coding: utf-8 -*-
from tensorflow import keras

# import library
# eng : ImageDataGenerator --> Generate batches of tensor image data with real-time data augmentation.
# tr : ImageDataGenerator --> derin öğrenme için görüntü verilerinin ardışık düzenlenmesi için başvurulan sınıf.
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os, random, shutil, time
import numpy as np

# eng : We describe the data augmentation techniques we use.
# tr : Kullanacağımız veri artırma tekniklerini tanımlıyoruz
datagen = ImageDataGenerator(rotation_range=45,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True,
                             vertical_flip=True,
                             fill_mode='constant')
n=0
path = 'C:/Users/Lab722-2080/python_image_enhancement-main/python_image_enhancement-main/test/'
path2 = 'C:/Users/Lab722-2080/python_image_enhancement-main/python_image_enhancement-main/reproduced_photos/'

files = os.listdir(path)
#files.remove ('desktop.ini')
print(files)


for i in files: #因為資料夾裡面的檔案都要重新更換名稱
    #print(i)
    img = load_img(path + i)
    z = str(n + 1).zfill(8)

    x = img_to_array(img)
    x = x.reshape((1,)+x.shape)

    ii = 0
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir=path2,
                              save_format='jpg'):
        ii+=1
        #time.sleep(1)
        if ii == 10:
            break
