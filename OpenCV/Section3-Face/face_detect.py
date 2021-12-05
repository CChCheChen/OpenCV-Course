import cv2 as cv

img = cv.imread('Resources/Photos/group 1.jpg')
# cv.imshow('Image to detect faces', img)

#Face detection dose not include face toner color, taking in only the gray scale image will do the work
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Image to detect faces gray', gray)

haar_cascade = cv.CascadeClassifier('Section3-Face/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=1)

cv.imshow('Detected Faces', img)

cv.waitKey(0)