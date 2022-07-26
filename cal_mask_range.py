'''import cv2
import  numpy as np

img=cv2.imread('F:/mask_dataset/RR/RR2_00000164.png',cv2.IMREAD_GRAYSCALE) #灰度图像
#img=cv2.imread('C:/Users/Lab722-2080/ZITS_inpainting-main/irregular_mask/mask_rates_40_50/0000095.png',cv2.IMREAD_GRAYSCALE) #灰度图像

x,y= img.shape
print(img.shape)

#遍历灰度图，阈值大于150的全变白
for i in range(x):
    for j in range(y):
        if img[i,j]>150:
            img[i,j]=255
        else:
            img[i,j]=0
black = 0
white = 0
#遍历二值图，为0则black+1，否则white+1
for i in range(x):
    for j in range(y):
        if img[i,j]==0:
            black+=1
        else:
            white+=1
print("白色个数:",white)
print("黑色个数:",black)
rate1 = white/(x*y)
rate2 = black/(x*y)
#round()第二个值为保留几位有效小数。
print("白色占比:", round(rate1*100,2),'%')
print("黑色占比:", round(rate2*100,2),'%')'''


import os, random, shutil,cv2

if __name__ == '__main__':
	frompath = 'F:/mask_dataset/RXX/'
	topath = 'F:/mask_dataset/strokes/'
	filepath = os.listdir(topath)	#mask range path
	filepath2 = os.listdir(frompath)
	a=b=c=d=e=f=0
	for n in filepath2:
		img = cv2.imread(frompath+n,cv2.IMREAD_GRAYSCALE)  # 灰度图像
		x, y = img.shape
		black = 0
		white = 0
		for i in range(x):
			for j in range(y):
				if img[i, j] == 0:
					black += 1
				else:
					white += 1
		rate1 = white / (x * y)
		#rate2 = black / (x * y)
		print(n, "白色占比:", round(rate1 * 100, 2), '%')