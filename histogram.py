# Import necessary libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Read the color image
img = cv.imread('./Resources/Photos/cats 2.jpg')
cv.imshow('img', img)
# creating a blank
blank=np.zeros(img.shape[:2],dtype='uint8')
# Convert the color image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)
circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,256,-1)
# cv.imshow('mask',mask)
mask=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('bit',mask)
# Grayscale histogram calculation
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

# Matplotlib plot for the grayscale histogram
'''plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()
'''
# color histogram
color=('b','g','r')
for i,col in enumerate(color):
    hist=cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0, 256])
plt.show()
# Wait for a key event and close all OpenCV windows
cv.waitKey(0)
