import os, random,shutil
filename="tomato"
path = 'D:/plant/'+filename+'/'
path2 = 'D:/plant_3part/train/'+filename+'/'
files = os.listdir(path)
if not os.path.isdir(path2):
    os.makedirs(path2)
list = list(range(0, 4872))
#x = len(list)
#print(x)
random.shuffle(list)
#print(list[2])

n = 0 #設定初始值
for i in files:
	oldname=path+files[n]
	filenumber=len(list)
	#sample = random.sample(range(0,filenumber), filenumber)
	z = str(list[n]).zfill(8)
	#print(z)
	newname=path2+filename+"_"+z+'.jpg'
	#shutil.copy(fileDir+name, tarDir+name) #複製
	os.rename(oldname,newname) #移動不會留下
	print(oldname+'>>>'+newname)
	n=n+1