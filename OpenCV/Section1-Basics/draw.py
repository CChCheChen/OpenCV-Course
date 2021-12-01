import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
#cv.imshow('Blank', blank)

#1. paint the image with color
# blank[:] = 0,255,0 #green
# blank[:] = 0,0,255 #red
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Paint color', blank)

#2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2)
# cv.imshow('Draw rectangle', blank)

#Drwa filled rectangle
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=-1)
# cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
# cv.imshow('Draw filled rectangle', blank)


#Draw filled rectangle based on image config
# cv.rectangle(blank, (blank.shape[1]//4, blank.shape[0]//3), (3*(blank.shape[1]//4), 2*(blank.shape[0]//3)), (0,255,0), thickness=-1)
# cv.imshow('Draw filled rectangle based on image config', blank)


#3. Draw cicrle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), blank.shape[1]//3, (0,0,255), thickness=3)
# cv.imshow('Draw circle', blank)

#Draw filled cicrle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), blank.shape[1]//5, (0,0,255), thickness=-1)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), blank.shape[1]//5, (0,0,255), thickness=cv.FILLED)
# cv.imshow('Draw filled circle', blank)

#4. Draw a line
cv.line(blank, (blank.shape[1]//4, blank.shape[0]//3), (3*(blank.shape[1]//4), 2*(blank.shape[0]//3)), (0,255,0), thickness=2)
# cv.imshow('Draw line', blank)

#5. Write text on image
cv.putText(blank, 'Hello, CChCheChen', (blank.shape[1]//5, blank.shape[0]//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)