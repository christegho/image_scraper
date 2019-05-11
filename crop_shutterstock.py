import glob
import cv2
from PIL import Image
import os

   
list_images = glob.glob('/data/gans/pills/SHUTTER*')

for image_path in list_images:
    print(image_path)
    try:
        im = Image.open(image_path)
        im.verify()
        im.close()
        img = cv2.imread(image_path)
        name = image_path.split('/')
        name[-1] = 'cropped_' + name[-1]
        crop_img = img[0:img.shape[0]-20, 0:img.shape[1]-15]
        cv2.imwrite('/'.join(name), crop_img)
    except:
        print('REMOVING', image_path)
        os.remove(image_path)