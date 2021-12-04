import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/group 1.jpg')
# cv.imshow('Group 1', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel Gradient Magnitude representation, in both x and y directions
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
# cv.imshow('Sobel X', sobelx)
# cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175) #more advanced method, as a multi-stage algorithm which uses the Sobel in it
cv.imshow('Canny', canny)

cv.waitKey(0)