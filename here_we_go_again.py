import cv2,os, glob
from pylab import *

origonal_path = 'C:/mushroom/T/'     # 原始圖片資料夾
croped_path = 'C:/mushroom/N_T/'    # 剪裁後圖片資料夾

if not os.path.isdir(croped_path):
    os.mkdir(croped_path)

path_list = os.listdir(origonal_path)
# print(path_list)
_ = 0
s = 0
resume_number = 0   # 中斷了可以設定你想重哪個圖開始繼續
cube_size = 224     # 基本大小
size_list = [224, 448, 896, 1792]    # 可調整大小

def show_xy(event,x,y,flags, papamer):
    global dot1, dot2, origonal_img, img2, n, cube_size, s
    if flags == 1:      # 左鍵按一下幫你畫框
        if event == 1:
            dot1 = [x, y]
            img2 = origonal_img.copy()
            cv2.rectangle(img2, (dot1[0] - int(cube_size/2), dot1[1] - int(cube_size/2)), (dot1[0] + int(cube_size/2), dot1[1] + int(cube_size/2)), (0, 0, 255), 2)
            cv2.imshow(n, img2)

    if flags == 2:      # 右鍵幫你調整框大小
        s += 1
        if s >= len(size_list):
            s = 0
        cube_size = size_list[s]

    if flags == 4:      # 中鍵兩下存檔
        if event == 9:
            crop_img = origonal_img[dot1[1] - int(cube_size/2):dot1[1] + int(cube_size/2), dot1[0] - int(cube_size/2):dot1[0] + int(cube_size/2)]
            # crop_img = cv2.resize(crop_img, (224, 224), interpolation=cv2.INTER_AREA)
            a = glob.glob(croped_path + n.replace('.jpg','') + '*.jpg')
            count = str(len(a))
            z = count.zfill(8)
            cv2.imwrite(croped_path + n.replace('.jpg','') + '_' + z + '.jpg', crop_img)
            print('save to: ' + croped_path + n.replace('.jpg','') + '_' + z + '.jpg')
    # 隨意鍵盤按鍵可以跳下一張圖

for n in path_list:
    _+=1
    if _ <= resume_number-1:
        continue
    origonal_img = None
    croped_img = None
    origonal_img = cv2.imread(origonal_path+n)

    dot1 = []

    if origonal_img.shape[1]<2560 and origonal_img.shape[0]<1440:     #判斷圖片大小會不會超過螢幕可顯示範圍 (正常尺寸 1920*1082 自己改)
        print(str(_)+' '+str(origonal_img.shape))
    elif origonal_img.shape[1]>2560 or origonal_img.shape[0]>1440:    #超過螢幕解析度就強只縮小圖片不然會看不到完整圖 (正常解析度是1920*1080 自己改)
        origonal_img2 = cv2.resize(origonal_img, (round(origonal_img.shape[1]/2), round(origonal_img.shape[0]/2)), interpolation=cv2.INTER_AREA)
        if origonal_img2.shape[1] > 2560 or origonal_img2.shape[0] > 1440:  # 二次檢查
            origonal_img2 = cv2.resize(origonal_img2,(round(origonal_img2.shape[1] / 2), round(origonal_img2.shape[0] / 2)),interpolation=cv2.INTER_AREA)
            print(str(_)+' '+str(origonal_img.shape) + '>>' + str(origonal_img2.shape))
            origonal_img=origonal_img2
        else:
            print(str(_)+' '+str(origonal_img.shape) + '>>' + str(origonal_img2.shape))
            origonal_img = origonal_img2

    cv2.imshow(n, origonal_img)
    cv2.moveWindow(n,0,0)     # 調整 origonal_img 顯示位置 可以自己調
    cv2.setMouseCallback(n, show_xy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

