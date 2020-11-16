import os
from cv2 import cv2 as cv
import numpy as np

people = ['Anna', 'Chenoa', 'Fari', 'Jolie', 'Keanu'] 
DIRTRAINING = r'/home/napspan/proyectos/git/python3/opencv1/faces/training'

haarCascade = cv.CascadeClassifier('haarFace.xml')

features = []
labels = []


def createTrain():
    for person in people:
        path = os.path.join(DIRTRAINING, person)
        label = people.index(person)

        for img in os.listdir(path):
            imgPath = os.path.join(path,img)

            imgArray = cv.imread(imgPath)
            gray = cv.cvtColor(imgArray, cv.COLOR_BGR2GRAY)

            facesRect = haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in facesRect:
                facesROI = gray[y:y+h, x:x+w]
                features.append(facesROI)
                labels.append(label)
createTrain()
print('training done')

# converting list to numpy arrays
features = np.array(features, dtype=object)
labels = np.array(labels) 

faceRecognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features and labels
faceRecognizer.train(features, labels)

faceRecognizer.save('faceTrained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
