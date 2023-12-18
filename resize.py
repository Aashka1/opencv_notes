import cv2 as cv
img=cv.imread('./Resources/Photos/cat_large.jpg')
cv.imshow('cat',img)
def rescaleFrame(frame,scale=0.75):
    # for already existing video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    d=(width,height)
    return cv.resize(frame,d,interpolation=cv.INTER_AREA)
resiimg=rescaleFrame(img,scale=.2)
cv.imshow('resize',resiimg)
def changeres(width,height):
    # for live video
    capture.set(3,width)
    capture.set(4,height)
capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_r=rescaleFrame(frame)
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    

        cv.imshow('Video', frame)
        cv.imshow('video',frame_r)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

# capture.release()
cv.destroyAllWindows()

cv.waitKey(0)