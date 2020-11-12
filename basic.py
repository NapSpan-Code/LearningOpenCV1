from cv2 import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#normal image
init=cv.imread('imagen/wppstalkerlarge.jpg')
img = rescaleFrame(init, 0.3)
cv.imshow('image', img)

#image to gray or template to other code
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

#blur
blur = cv.GaussianBlur(img, (1,1), cv.BORDER_DEFAULT)
#cv.imshow('blur', blur)

#EdgeCascade
canny=cv.Canny(blur, 125, 175)
cv.imshow('canny', canny)

#Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dilated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded', eroded)

#resize ignoring aspect-ratio
resized = cv.resize(init, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#cropping
cropped = img[0:50, 50:100]
cv.imshow('cropped', cropped)

cv.waitKey(0)
