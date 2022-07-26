import os, random, shutil, cv2

frompath = 'F:/Imagenet/imagenet21k_resized/imagenet21k_val/'
topath = 'F:/Imagenet/imagenet21k_resized/imagenet_test_10000/'

if __name__ == '__main__':
	frompathfile = os.listdir(frompath)
	#print(frompathfile)
	file_number = len(frompathfile)
	for n in range(file_number):
		pathDir = os.listdir(frompath+frompathfile[n]+'/')
		#picknumber=int(filenumber*rate) #按照rate比例從資料夾中取一定數量圖片 filenumber*rate
		sample = random.sample(pathDir, 1)  #隨機選取picknumber數量的樣本圖片
		print (sample)
		for name in sample:
			shutil.copy(frompath+frompathfile[n]+'/'+name, topath+name) #複製
			#os.rename(fileDir + name, tarDir + name)  # 剪下貼上

'''if __name__ == '__main__': #test gray image
	file = os.listdir(topath)
	filen = len(file)
	nn=0
	for n in range(filen):
		image = cv2.imread(topath+file[n])
		if(image.shape[2]==1):
			print(file[n])
		if (image.shape[2] == 3):
			nn+=1
	print(nn)'''

