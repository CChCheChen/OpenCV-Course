import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)
#******************Mask must be the same size as the original image******************

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)

mask_circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2 - 50), 100, 255, -1)
# cv.imshow('Mask Circle', mask_circle)

mask_rectangle= cv.rectangle(blank.copy(), (img.shape[1]//4, img.shape[0]//4), (3*(img.shape[1]//4), 3*(img.shape[0]//4)), 255, -1)
# cv.imshow('Mask Rectangle', mask_rectangle)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
mask_weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Mask weird shape', mask_weird_shape)

# masked = cv.bitwise_and(img, img, mask=mask_circle)
# masked = cv.bitwise_and(img, img, mask=mask_rectangle)
masked = cv.bitwise_and(img, img, mask=mask_weird_shape)
cv.imshow('Masked', masked)

cv.waitKey(0)