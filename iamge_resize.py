#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import os


path = 'F:/mask_dataset/strokes/strokes_1+10/'
path2 ='F:/mask_dataset/RR/'
file = os.listdir(path)
file_n = len(file)
list = []
x = 8
xWx = 0
pad = '0'

for n in file:
    img = Image.open(path+n)
    (w, h) = img.size
    #print('w=%d, h=%d', w, h)
    #img.show()

    new_img = img.resize((256, 256))
    #new_img.show()
    new_img.save(path+n)
