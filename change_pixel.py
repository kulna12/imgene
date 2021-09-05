import os,sys
import glob
import cv2

folder = input('Enter Folder Name : ')
width =  int(input('Width : '))
height = int(input('Height : '))
os.mkdir('resized')
folderLen = len(folder)
try:
     for img in glob.glob(folder + '/*.png'):
            image =  cv2.imread(img)
            imgResize =  cv2.resize(image, (width, height))
            print("Saving Picture of : ", imgResize.shape)
            cv2.imwrite('resized' + img[folderLen:] , imgResize)
            
except Exception as err:
     print(err)
