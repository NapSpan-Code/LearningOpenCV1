from cv2 import cv2 as cv
import numpy as np

#void image to read on
blank = np.zeros((500,500,3), dtype='uint8')

#blank[:] = 0,255,0
#cv.imshow('Green', blank)

#rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

#circle
cv.circle(blank, (250,250),50, (255,0,0), thickness=2)
cv.imshow('Circle', blank)

#line
cv.line(blank,(500,500), (250,250), (0,0,255), thickness=1)
cv.imshow('Line', blank)

#text
cv.putText(blank, 'Hello OpenCV', (100,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=1)
cv.imshow('text', blank)
cv.waitKey(0)