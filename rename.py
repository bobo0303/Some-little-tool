'''import os
import random
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


path = 'F:/mask_dataset/R/'
path2 ='F:/mask_dataset/RR/'
file = os.listdir(path)
file_n = len(file)
file2 = os.listdir(path2)
file_n2 = len(file)
list = []
nn=0

for n in file:
    z = str(nn).zfill(8)
    os.rename(path+n,path+"RRx3_"+z+'.png')
    nn+=1'''

import os

path = 'F:/mask_dataset/strokes/'
file = os.listdir(path)
xx = 0


for n in file:
    file2 = os.listdir(path+n)
    print(n)
    xx =0
    for nn in file2:
        #print(nn)
        z = str(xx).zfill(8)
        os.rename(path+n+'/'+nn, path+n+'/'+n+'_'+z+'.png')
        xx+=1


