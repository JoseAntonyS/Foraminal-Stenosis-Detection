#This file generates sufficient data from the originally given data for training.
import cv2
import os
import random
import numpy as np

def rotate_images(image, scale=1.0, w=320, h=230):
    center = (h / 2, w / 2)
    angle = random.randint(-13, 13)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated
    
def blur(image):
    x = random.randrange(1, 6, 2)
    blur = cv2.GaussianBlur(image, (x, x), cv2.BORDER_DEFAULT)
    return blur


def flip_image(image):
    flip= np.fliplr(image)
    return flip
    
def translation(image):
    x = random.randint(-50, 50)
    y = random.randint(-50, 50)
    rows, cols, z = image.shape
    M = np.float32([[1, 0, x], [0, 1, y]])
    translate = cv2.warpAffine(image, M, (cols, rows))
    return translate
    
def load_images(folder):
    
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            
            rot=rotate_images(img)
            cv2.imwrite("./aug_org_images/"+filename+"rotate.png", rot)
            bl=blur(img)
            cv2.imwrite("./aug_org_images/"+filename+"blur.png", bl)
            trans= translation(img)
            cv2.imwrite("./aug_org_images/"+filename+"trans.png", trans)           
            flp = flip_image(img)
            cv2.imwrite("./aug_org_images/"+filename+"flip.png", flp)
    return rot,bl,flp,trans
root_dir='./aug_org_images'
result=load_images(root_dir)
