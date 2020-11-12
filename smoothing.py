from cv2 import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


init = cv.imread('imagen/wppstalkerlarge.jpg')
img = rescaleFrame(init, 0.3)
cv.imshow('stalker', img)

#Averaging blur
average = cv.blur(img, (3,3))
cv.imshow('averageblur', average)

#Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussianBlur', gauss)

#Median Blur (good for Computer Vision)
medianBlur = cv.medianBlur(img, 3)
cv.imshow('medianBlur', medianBlur)

#Bilateral Blur (good as well for Computer Vision)
biBlur = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateralBlur', biBlur)

cv.waitKey(0)