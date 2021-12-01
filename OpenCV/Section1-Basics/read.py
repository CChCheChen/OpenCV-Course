import cv2 as cv

#----------Reading images----------
# img = cv.imread('Resources/Photos/cat.jpg')
# imgL = cv.imread('Resources/Photos/cat_large.jpg')

# cv.imshow('Cat', img)
# cv.imshow('Cat Large', imgL)

# cv.waitKey(0)

#----------Reading videos----------
#capture = cv.VideoCapture(0) #for connecting your webcam
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    
    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'): #close window when 'd' is pressed on keyboard
            break
    else:
        break

capture.release()
cv.destroyAllWindows()