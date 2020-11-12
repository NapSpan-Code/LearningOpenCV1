from cv2 import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#getting image
init = cv.imread('imagen/wppstalkerlarge.jpg')
img = rescaleFrame(init, 0.4)
cv.imshow('stalker', img)

#creating mask
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2 + 60,img.shape[0]//2 - 50), 100, 255, -1)
cv.imshow('Mask', mask)

#making grayscale version
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#masking grayscale image
#maskedImage = cv.bitwise_and(gray,gray,mask=mask)
#cv.imshow('MaskedApplied', maskedImage)

#Grayscale histogram
#grayHist = cv.calcHist([gray],[0], maskedImage, [256], [0,256])

#plt.figure()
#plt.title('Grayscale Histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(grayHist)
#plt.xlim([0,256])
#plt.show()


#histograms with color
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
#masking color image
maskedImage = cv.bitwise_and(img,img,mask=mask)
cv.imshow('MaskedApplied', maskedImage)

for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)