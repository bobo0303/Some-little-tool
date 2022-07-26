import os
import cv2

'''path = 'C:/Users/lab722-2080/image_inpainting/25_celeba/datasets/CelebA/CelebA_1+10/' #這就是欲進行檔名更改的檔案路徑，路徑的斜線是為/，要留意下！
files = os.listdir(path)
n = 0 #設定初始值
for i in files: #因為資料夾裡面的檔案都要重新更換名稱
	img = cv2.imread(path+files[n], cv2.IMREAD_GRAYSCALE)
	#img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
	dst = 255 - img
	z = str(n+1).zfill(8)
	newname='C:/Users/lab722-2080/image_inpainting/25_celeba/datasets/CelebA/color_change/CelebA_1+10/'+'CelebA_test_'+ z +'_mask'+'.png' #在本案例中的命名規則為：年份+ - + 次序，最後一個.wav表示該檔案的型別
	cv2.imwrite(newname, dst)
	n=n+1 #當有不止一個檔案的時候，依次對每'''

frompath = 'F:/Imagenet/imagenet21k_resized/fortest/ImageNet_mask_40+50/' #這就是欲進行檔名更改的檔案路徑，路徑的斜線是為/，要留意下！
topath = 'F:/Imagenet/imagenet21k_resized/fortest/color_change/ImageNet_mask_40+50/'

files = os.listdir(frompath)
n=0
if not os.path.isdir(topath):
	os.makedirs(topath)
for i in files:
	img = cv2.imread(frompath+i, cv2.IMREAD_GRAYSCALE)
	#img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
	dst = 255 - img
	z = str(n).zfill(8)
	newname=topath+'ImageNet_'+ z +'_mask'+'.png' #在本案例中的命名規則為：年份+ - + 次序，最後一個.wav表示該檔案的型別
	cv2.imwrite(newname, dst)
	n=n+1 #當有不止一個檔案的時候，依次對每'''


