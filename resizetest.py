from cv2 import cv2 as cv


#img = cv.imread('imagen/wppstalkerlarge.jpg')
#cv.imshow('STALKERFAT', img)


#Reescalating function works with wathever
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#life video
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)

#Reading Videos
capture = cv.VideoCapture('video/shrek.mp4')

while True:
    isTrue, frame = capture.read()

    frameResized = rescaleFrame(frame, scale=0.5)

    cv.imshow('Video',frame)
    cv.imshow('VideoResized',frameResized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()