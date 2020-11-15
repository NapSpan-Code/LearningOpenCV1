from cv2 import cv2 as cv

init = cv.imread('imagen/lady.jpg')
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
img = rescaleFrame(init, 0.5)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#haarCascade loading classifier
haarCascade = cv.CascadeClassifier('haarFace.xml')

facesRect = haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

print(f'number of faces = { len(facesRect) }')

#print faces in image

for (x,y,w,h) in facesRect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=3)

cv.imshow('detectedFaces', img)

devsImageInit = cv.imread('imagen/aBunchOfDevs.jpg')
devsImage = rescaleFrame(devsImageInit, 0.5)
devsGray = cv.cvtColor(devsImage, cv.COLOR_BGR2GRAY)

facesDevsRect = haarCascade.detectMultiScale(devsGray, scaleFactor=1.1, minNeighbors=2)
print(f'number of faces = { len(facesDevsRect) }')

for (x,y,w,h) in facesRect:
    cv.rectangle(devsImage, (x,y), (x+w,y+h), (0,255,0), thickness=1)

cv.imshow('detectedDevsFaces', devsImage)

cv.waitKey(0)

#Note: Algorithms are clearly delicate, any weird face will not be recognized
#This seems quite crappy