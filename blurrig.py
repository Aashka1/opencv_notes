import cv2 as cv
img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats', img)
# averaging 
average=cv.blur(img,(3,3))
cv.imshow('average',average)
# gaussian blur
gauss_blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('gassina blur',gauss_blur)
# median blur
medin=cv.medianBlur(img,3)
cv.imshow('median',medin )
# bilateral->most effective
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral',bilateral)
cv.waitKey(0)