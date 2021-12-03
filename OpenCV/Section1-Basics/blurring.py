import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

# Averaging Blur
# average = cv.blur(img, (3,3))
# cv.imshow('Average Blur', average)
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral Blur ---- the most effective, with the retained edges
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)