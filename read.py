from cv2 import cv2 as cv

#Loads an image
#img = cv.imread('imagen/gato.jpg')

#cv.imshow('Gato', img)

#cv.waitKey(0)

#Loads a video

capture = cv.VideoCapture('video/shrek.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()