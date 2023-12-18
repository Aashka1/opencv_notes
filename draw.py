import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# This line creates a NumPy array representing a blank image. 
# The array has dimensions 500x500 pixels and 3 channels (representing the RGB color space).
#  The dtype='uint8' specifies that each pixel's value should be an unsigned 8-bit integer//the data type of an img.
''' 1. Paint the image a certain colour'''
blank[200:300, 300:400] = 0,0,255
cv.imshow('Green', blank)
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=8)
''' (blank.shape[1] // 2, blank.shape[0] // 2): This is the coordinate of the bottom-right corner of the rectangle.
blank.shape[1] gives the width of the image, and blank.shape[0] gives the height. So, (blank.shape[1] // 2, blank.shape[0] // 2) 
is the bottom-right corner, and it's set to be half of the width and half of the height of the image. 
This means the rectangle will cover the top-left quarter of the image.'''
cv.imshow('rectangle',blank)
# 3. Draw A circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255,0,255), thickness=-1)
cv.imshow('Circle', blank)
# 5. Write text
cv.line(blank,(0,0),((blank.shape[1]//2),(blank.shape[0]//2)) ,(255,255,255),thickness=2)
cv.imshow('line',blank)
#5. write text
cv.putText(blank,'hello',(0,255),cv.FONT_HERSHEY_DUPLEX,1.0,(255,255,0),thickness=2)
cv.imshow('text',blank)
cv.imshow('Blank', blank)
cv.waitKey(0)
cv.destroyAllWindows()
