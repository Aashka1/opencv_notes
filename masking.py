# Importing the OpenCV library with an alias 'cv' and NumPy with an alias 'n'.
import cv2 as cv
import numpy as n

# Reading an image from the specified file path.
img = cv.imread('./Resources/Photos/cats.jpg')

# Displaying the original image.
cv.imshow('img', img)

# Creating a blank (black) image with the same dimensions as the original image.
blank = n.zeros(img.shape[:2], dtype='uint8')

# Displaying the blank image.
cv.imshow('blank', blank)

# Creating a circular mask on the blank image. The center of the circle is at the center of the original image,
# and the radius is set to 100. The mask is assigned pixel values of 255 (white) inside the circle and 0 (black) outside.
'''mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)'''

# Creating a circular region on a black background using a copied blank image.
circle = cv.circle(blank.copy(), (img.shape[1] // 2+45, img.shape[0] // 2), 100, 255, -1)

# Creating a rectangular region on a black background using a copied blank image.
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

# Combining the circular and rectangular regions using bitwise AND operation.
wierd = cv.bitwise_and(circle, rectangle)

# Displaying the combined image showing both circular and rectangular regions.
cv.imshow('weird', wierd)

# Applying the created combined mask to the original image using bitwise AND operation.
masked = cv.bitwise_and(img, img, mask=wierd)

# Displaying the masked image, where only the region inside the combined mask is visible (overlap of circular and rectangular regions).
cv.imshow('masked', masked)

# Waiting for a key event to close the displayed windows.
cv.waitKey(0)
