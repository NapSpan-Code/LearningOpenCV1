from cv2 import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

init = cv.imread('imagen/wppstalkerlarge.jpg')
img = rescaleFrame(init, 0.4)
cv.imshow('stalker', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2 + 60,img.shape[0]//2 - 50), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('maskedImage', masked)





cv.waitKey(0)