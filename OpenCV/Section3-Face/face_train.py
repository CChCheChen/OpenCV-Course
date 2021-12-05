import cv2 as cv
import numpy as np
import os

# people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

people = []
for i in os.listdir('Resources/Faces/train'):
    people.append(i)
# print(people)

DIR = r'Resources/Faces/train'

haar_cascade = cv.CascadeClassifier('Section3-Face/haar_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
# print(f'length of the features = {len(features)}')
# for f in features:
#     print(f)
# print(f'length of the labels = {len(labels)}')
# for l in labels:
#     print(l)
print('--------------- Training done ---------------')

#Convert features and labels list to Numpy arrays
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features,labels)# Train the Recognizer on the features list and the labels list

face_recognizer.save('Section3-Face/face_trained.yml')
np.save('Section3-Face/features.npy', features)
np.save('Section3-Face/labels.npy', labels)