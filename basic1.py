import cv2 as cv
img=cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('im',img)
# Converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
# blur an image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
# edge cascade
canny=cv.Canny(img,125,175)
cv.imshow('canny',canny)
# Dilating the image
dilated=cv.dilate(canny,(13,13),iterations=1)
cv.imshow('dilated',dilated)
# eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)
# resize
resized =cv.resize(img,(500,500),interpolation=cv.INTER_AREA)#cv.inter_linerar->for higher resize than original pic or inter_cubic which gives better quality than linear and area

cv.imshow('rezied',resized)
# cropping
crop=img[50:200,200:400]
cv.imshow('crop',crop)
cv.waitKey(0)
