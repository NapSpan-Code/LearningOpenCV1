from cv2 import cv2 as cv
import numpy as np

img = cv.imread('imagen/wppstalkerlarge.jpg')

cv.imshow('stalker', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

grayblurred = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

#corners
canny = cv.Canny(grayblurred, 125, 175)
cv.imshow('CannyEdges', canny)
#corners can also be found by threesholding

#threeshold
#ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#cv.imshow('Thresh', thresh)

#contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('contoursDrawn', blank)

cv.waitKey(0)