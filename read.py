import cv2 as cv

img = cv.imread('imagen/gato.jpg')

cv.imshow('Gato', img)

cv.waitKey(0)
