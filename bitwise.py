from cv2 import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#bitwise AND. Exactly what you imagine
bitwiseAND = cv.bitwise_and(rectangle, circle)
cv.imshow('bitWiseAND', bitwiseAND)

#bitwise OR
bitwiseOR = cv.bitwise_or(rectangle, circle)
cv.imshow('bitWiseOR', bitwiseOR)

#bitwise XOR
bitwiseXOR = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwiseXOR', bitwiseXOR)

#bitwise NOT
bitwiseNOT = cv.bitwise_not(bitwiseXOR)
cv.imshow('bitwisenot', bitwiseNOT)

cv.waitKey(0)
