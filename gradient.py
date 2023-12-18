import cv2 as cv
import numpy as np
img=cv.imread('./Resources/Photos/cat.jpg')
cv.imshow('cat',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# laplacion
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('laplacin',lap)
# sobel
sobel_x=cv.Sobel(gray,cv.CV_64F,1,0)
sobel_y=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobel_x,sobel_y)
cv.imshow("sobelx",sobel_x)
cv.imshow('sobey',sobel_y)
cv.imshow('combined_sobel',combined_sobel)
# canny
canny=cv.Canny(gray,150,175)
cv.imshow('Canny',canny)
cv.waitKey(0)