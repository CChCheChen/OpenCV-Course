import cv2 as cv

#This function will work for images, videos and live videos
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#This function only works form live videos
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

#----------Resizing images----------
imgL = cv.imread('Resources/Photos/cat_large.jpg')
img_resized = rescaleFrame(imgL, scale=.2)
cv.imshow('Cat', imgL)
cv.imshow('Cat Resized', img_resized)
cv.waitKey(0)

#----------Resizing videos----------
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    
    if isTrue:
        frame_resized = rescaleFrame(frame, scale=.2)
        cv.imshow('Video', frame)
        cv.imshow('Video Resized', frame_resized)
        if cv.waitKey(20) & 0xFF==ord('d'): #close window when 'd' is pressed on keyboard
            break
    else:
        break
    
capture.release()
cv.destroyAllWindows()