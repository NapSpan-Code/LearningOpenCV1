from cv2 import cv2 as cv

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
capture = cv.VideoCapture(0)


while True:
    isTrue, frame = capture.read()
    cv.putText(frame, 'Hello World', (0,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=1)


    frameResized = rescaleFrame(frame, scale=0.5)

    cv.imshow('Video',frame)
    cv.imshow('VideoResized',frameResized)

    #Let's find the contour
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
    cv.imshow('blurred', blurred)
    canny = cv.Canny(blurred, 50, 150)
    cv.imshow('canny', canny)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()