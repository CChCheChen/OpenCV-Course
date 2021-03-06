import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/lady.jpg')
# cv.imshow('Lady', img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

#----------Find edge cascades---------- 
canny = cv.Canny(blur, 125, 175)
# canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contour(s) found!')

# cv.RETR_LIST return all contours
# cv.RETR_EXTERNAL return only external contours
# cv.RETR_TREE return all hierarchical contours, which are in a hierarchical system

# Contour approximation method
# cv.CHAIN_APPROX_NONE return all contours --- line example, this returns all points on the line
# cv.CHAIN_APPROX_SIMPLE compresses all contours in a simple ones that make most sense  --- line example, this returns 2 end points of the line

#----------Binarize the image----------
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)

cv.waitKey(0)