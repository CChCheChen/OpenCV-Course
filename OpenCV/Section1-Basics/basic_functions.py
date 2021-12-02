import cv2 as cv
img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

#convert image to greyscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Grey scale', grey)

#Blur image
#blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)#more blurry
#cv.imshow('Blur', blur)

#Edge cascade
#canny = cv.Canny(img, 125, 175)
canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny', canny)

#Dilating the image
#dilate = cv.dilate(canny, (3,3), iterations=1)
#dilate = cv.dilate(canny, (7,7), iterations=1)
dilate = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilate', dilate)

#Eroding the image - reverse of Dilating
#eroded = cv.erode(dilate, (3,3), iterations=1)
eroded = cv.erode(dilate, (7,7), iterations=3) 
#cv.imshow('Eroded', eroded)

#Resize
#resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
resized = cv.resize(img, (500,500))
#cv.imshow('Resized', resized)

#Cropping - (x1,y1) as the top-left vertex and (x2,y2) as the bottom-right vertex of a rectangle region within that image, then [y1:y2, x1:x2]
#cropped = img[50:200, 200:400]
# print(img.shape[0])#height
# print(img.shape[1])#width
cropped = img[(img.shape[0]//3):2*(img.shape[0]//3), (img.shape[1]//3):2*(img.shape[1]//3)] #(x1,y1) = (img.shape[1]//3, img.shape[0]//3) & (x2,y2) = (2*(img.shape[1]//3), 2*(img.shape[0]//3))
cv.imshow('Cropped', cropped)

cv.waitKey(0)