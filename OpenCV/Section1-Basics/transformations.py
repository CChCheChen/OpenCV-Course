import cv2 as cv
import numpy as np
img = cv.imread('Resources/Photos/lady.jpg')
#cv.imshow('Lady', img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#-x --> left
#-y --> up
#x ---> right
#y ---> down

#translated = translate(img, 100, 100) #right 100px and down 100px
translated = translate(img, -100, 100) #left 100px and down 100px
#cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

#rotated = rotate(img, 45) #counterclockwise
rotated = rotate(img, -45) #clockwise
#cv.imshow('Rotated', rotated)

#these 2 below are different
rotated_img_90 = rotate(img, -90)
rotated_rotated_45 = rotate(rotated, -45)
#cv.imshow('Rotated Img -90', rotated_img_90)
#cv.imshow('Rotated Rotated -45', rotated_rotated_45)

#Resize
#resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) #shrinking the image
resized_linear = cv.resize(img, (1500,1500), interpolation=cv.INTER_LINEAR) #enlarging the image
resized_cubic = cv.resize(img, (1500,1500), interpolation=cv.INTER_CUBIC) #enlarging the image, slow process but better result with high quality
#cv.imshow('Resized linear', resized_linear)
#cv.imshow('Resized cubic', resized_cubic)

#Flip
flip_vertically = cv.flip(img, 0) # 0 is flipping over x-axis vertically
flip_horizontally = cv.flip(img, 1) # 1 is flipping over y-axis horizontally
flip_both = cv.flip(img, -1) #-1 is flipping both vertically and horizontally
# cv.imshow('flip vertically', flip_vertically)
# cv.imshow('flip horizontally', flip_horizontally)
# cv.imshow('flip vertically & horizontally', flip_both)

#Cropping
cropped = img[(img.shape[0]//3):2*(img.shape[0]//3), (img.shape[1]//3):2*(img.shape[1]//3)] #(x1,y1) = (img.shape[1]//3, img.shape[0]//3) & (x2,y2) = (2*(img.shape[1]//3), 2*(img.shape[0]//3))
cv.imshow('Cropped', cropped)

cv.waitKey(0)