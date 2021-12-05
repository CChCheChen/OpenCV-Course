import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('Section3-Face/haar_face.xml')
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# features = np.load('Section3-Face/features.npy', allow_pickle=True)
# labels = np.load('Section3-Face/labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Section3-Face/face_trained.yml')

# img = cv.imread('Resources/Faces/val/jerry_seinfeld/3.jpg')
# img = cv.imread('Resources/Faces/val/madonna/1.jpg') #failed
# img = cv.imread('Resources/Faces/val/madonna/4.jpg')
# img = cv.imread('Resources/Faces/val/elton_john/5.jpg') #failed
img = cv.imread('Resources/Faces/val/elton_john/3.jpg')
# img = cv.imread('Resources/Faces/val/ben_afflek/5.jpg')
# img = cv.imread('Resources/Faces/val/mindy_kaling/4.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in img
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=1)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow(str(people[label]), img)

cv.waitKey(0)