import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/lady.jpg')
# cv.imshow('Lady', img)

# pixel intensity < threshold --> pixel intensity = 0
# pixel intensity > threshold --> pixel intensity = 255, white

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Simple thresholding
threshold1, thresh1 = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) #thresh is the converted image, threshold is still 150
# cv.imshow('Simple thresholded 1', thresh1)
# threshold2, thresh2 = cv.threshold(gray, 100, 255, cv.THRESH_BINARY) #thresh is the converted image, threshold is still 100 --> result is more white
# cv.imshow('Simple thresholded 2', thresh2)
# threshold3, thresh3 = cv.threshold(gray, 200, 255, cv.THRESH_BINARY) #thresh is the converted image, threshold is still 200 --> result is more black
# cv.imshow('Simple thresholded 3', thresh3)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) #black pixel changed to white, white pixel changed to black
# cv.imshow('Simple thresholded inverse', thresh_inv)

# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)
# adaptive_thresh_alt1 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 3)
# cv.imshow('Adaptive Thresholding ALT 1', adaptive_thresh_alt1)
# adaptive_thresh_alt2 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 1)
# cv.imshow('Adaptive Thresholding ALT 2', adaptive_thresh_alt2)
# adaptive_thresh_alt3 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
# cv.imshow('Adaptive Thresholding ALT 3', adaptive_thresh_alt3)
adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Thresholding inverse', adaptive_thresh_inv)

adaptive_thresh_Gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding Gaussian', adaptive_thresh_Gaussian)

cv.waitKey(0)