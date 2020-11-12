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
    cv.putText(frame, 'Jorge Crespo Sueiro, Puto Amo', (0,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=1)


    frameResized = rescaleFrame(frame, scale=0.5)

    cv.imshow('Video',frame)
    cv.imshow('VideoResized',frameResized)

    #EdgeCascade
    canny=cv.Canny(frame, 150, 150)
    cv.imshow('canny', canny)

    #flipped
    flipped = cv.flip(frameResized, 1)
    cv.imshow('flipped', flipped)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()