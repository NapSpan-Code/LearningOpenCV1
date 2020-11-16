from cv2 import cv2 as cv
import numpy as np

haarCascade = cv.CascadeClassifier('haarFace.xml')

people = ['Anna', 'Chenoa', 'Fari', 'Jolie', 'Keanu']
#features = np.load('features.npy')
#labels = np.load('labels.npy')

faceRecognizer = cv.face.LBPHFaceRecognizer_create()
faceRecognizer.read('faceTrained.yml')

img = cv.imread(r'/home/napspan/proyectos/git/python3/opencv1/faces/validation/Fari/fariVal1.jpg')

gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)


#detect face
facesRect = haarCascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=4)

for (x,y,w,h) in facesRect:
    facesROI = gray[y:y+h, x:x+h]

    label, confidence = faceRecognizer.predict(facesROI)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0),thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected face', img)
cv.waitKey(0)