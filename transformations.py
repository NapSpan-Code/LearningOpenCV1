from cv2 import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


init = cv.imread('imagen/wppstalkerlarge.jpg')
img = rescaleFrame(init,0.5)


cv.imshow('image', img)

#Translation "flipping images"

def translate(image, x, y):
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatrix, dimensions)

# -x -> Left
# -y -> Up
# +x -> Right
# +y -> Down

translated = translate(img, -100, -100)
cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMatrix, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #explore the other interpolation methods
cv.imshow('resized', resized)

#Flipping
fliped = cv.flip(img, 0)# 0 vertically, 1 horizontally, -1 both
cv.imshow('flipped', fliped)

#cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)