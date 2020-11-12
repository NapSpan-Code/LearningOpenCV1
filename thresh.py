from cv2 import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#getting image
init = cv.imread('imagen/wppstalkerlarge.jpg')
img = rescaleFrame(init, 0.4)
cv.imshow('stalker', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRay', gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('threshImaged', thresh)

threshold, threshInv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('threshImagedInverse', threshInv)

#Adaptive Thresholding
adaptiveThresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5)
cv.imshow('adaptive thresholding', adaptiveThresh)


cv.waitKey(0)