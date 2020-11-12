from cv2 import cv2 as cv
import numpy as np

img = cv.imread('imagen/wppstalkerlarge.jpg')
cv.imshow('gato2stalker', img)

b,g,r = cv.split(img)
# displayed in grayscale based on the intensity of each colour
cv.imshow('blue', b)
cv.imshow('red', g)
cv.imshow('green', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#toMerge
merged = cv.merge([b,g,r])
cv.imshow('Merged image', merged)

#see actual color
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('tblue', blue)
cv.imshow('tgreen', green)
cv.imshow('tred', red)



cv.waitKey(0)