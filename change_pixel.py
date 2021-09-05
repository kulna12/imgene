import os,sys
import glob
import cv2

def  change_pixel(folder, width, height):
    folderLen = len(folder)
    os.mkdir('resized')
    try:
        for img in glob.glob(folder + '/*.png'):
            imgage =  cv2.imread(img)
            imgResize =  cv2.resize(image, (width, height))
            print("Saving Picture of : ", imgResize.shape)
            cv2.imwrite('resized' + img[folderLen:] , imgRe)
            
   except Error as err  :
       return err


def main():
    folder =  input('Enter folder name :   ')
    width = input(int('Width : '))
    height = input(int('Height : '))        
    change_pixel(folder, width, height)

if __name__ == '__main__':
    main()
    sys.exit(0)
