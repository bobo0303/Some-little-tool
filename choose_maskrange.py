import os, random, shutil,cv2

if __name__ == '__main__':
	frompath = 'F:/mask_dataset/RR/'
	topath = 'F:/mask_dataset/strokes/'
	filepath = os.listdir(topath)	#mask range path
	filepath2 = os.listdir(frompath)
	a=b=c=d=e=f=0
	aa = len(os.listdir(topath + filepath[0]))
	bb = len(os.listdir(topath + filepath[1]))
	cc = len(os.listdir(topath + filepath[2]))
	dd = len(os.listdir(topath + filepath[3]))
	ee = len(os.listdir(topath + filepath[4]))
	ff = len(os.listdir(topath + filepath[5]))

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
		print("白色占比:", round(rate1 * 100, 2), '%')
		#print("黑色占比:", round(rate2 * 100, 2), '%')
		rate1 = rate1 * 100
		if rate1 < 10:
			os.rename(frompath + n, topath + filepath[0] + '/' + n)
			#print(topath + filepath[0] + '/' + n)
			a+=1
		elif rate1>10 and rate1<20:
			os.rename(frompath + n, topath + filepath[1] + '/' + n)
			#print(topath + filepath[1] + '/' + n)
			b+=1
		elif rate1>20 and rate1<30:
			os.rename(frompath + n, topath + filepath[2] + '/' + n)
			#print(topath + filepath[2] + '/' + n)
			c+=1
		elif rate1>30 and rate1<40:
			os.rename(frompath + n, topath + filepath[3] + '/' + n)
			#print(topath + filepath[3] + '/' + n)
			d+=1
		elif rate1>40 and rate1<50:
			os.rename(frompath + n, topath + filepath[4] + '/' + n)
			#print(topath + filepath[4] + '/' + n)
			e+=1
		elif rate1>50 and rate1<60:
			os.rename(frompath + n, topath + filepath[5] + '/' + n)
			#print(topath + filepath[5] + '/' + n)
			f+=1
	print(filepath[0]+' = '+ str(a),filepath[1]+' = '+ str(b),filepath[2]+' = '+ str(c),filepath[3]+' = '+ str(d),filepath[4]+' = '+ str(e),filepath[5]+' = '+ str(f))


	'''if not os.path.isdir(topath):
		os.makedirs(topath)

	pathDir = os.listdir(frompath)    #取圖片的原始路徑
	filenumber=len(pathDir)
	rate=0.516    #自定義抽取圖片的比例，比方說100張抽10張，那就是0.1
	picknumber=int(filenumber*rate) #按照rate比例從資料夾中取一定數量圖片
	sample = random.sample(pathDir, 10450)  #隨機選取picknumber數量的樣本圖片

	nn = 0
	for name in sample:
		z = str(nn).zfill(8)
		shutil.copy(frompath+name, topath+'iamgenet_mask_'+z+'.png') #複製
		#os.rename(fileDir+name, tarDir+name) #剪下貼上
		nn+=1
		print(topath+'ImageNet_mask_'+z+'.png')
	print('done!')'''
