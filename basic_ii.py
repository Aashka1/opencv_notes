import cv2 as cv
import numpy as np
img=cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('im',img) 
# Translation->shifting of img in x or y direction
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimension=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)
# for rotating the img
def rotate(img,angle,rot=None):
    width,height=img.shape[:2]
    if rot==None:
        rot=(width//2,height//2)
    rot=cv.getRotationMatrix2D(rot,angle,1.0)
    di=(width,height)
    return cv.warpAffine(img,rot,di)
rotatee=rotate(img,45)
cv.imshow('rotated',rotatee)
# for resizing
resize=cv.resize(img,(250,250),interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resize)
# for flip
flip=cv.flip(img,0)
'''
0-fliping vertically
1-flipping horizonatlly
-1= flipping both vertically horizontally
'''
cv.imshow('flip',flip)
# crop
cropp=img[200:400.300:400]
cv.imshow('crop',cropp)
cv.waitKey(0)
