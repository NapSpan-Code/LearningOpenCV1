from cv2 import cv2 as cv

img = cv.imread('imagen/gato.jpg')
cv.imshow('Gato', img)


# #BGR2GRAY
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# #BGR2HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# #BGR2L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# inversion BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

#Note: It's possible to convert them back

cv.waitKey(0)