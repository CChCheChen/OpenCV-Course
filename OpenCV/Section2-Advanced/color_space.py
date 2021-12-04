import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/lady.jpg')
# cv.imshow('Lady', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to LAB/L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', rgb)
# plt.imshow(rgb)
# plt.show()

# it could be from Grayscale/HSV/LAB/L*A*B/RGB to BGR
# but can not from, for example from Grayscale to HSV, Grayscale must be converted into BGR first, then BGR to HSV
# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('hsv_bgr', hsv_bgr)

# LAB/L*A*B to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
# cv.imshow('lab_bgr', lab_bgr)

# LAB/L*A*B to HSV
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab_bgr', lab_bgr)
lab_bgr_hsv = cv.cvtColor(lab_bgr, cv.COLOR_BGR2HSV)
cv.imshow('lab_bgr_hsv', lab_bgr_hsv)

cv.waitKey(0)

# plt.imshow(img)
# plt.show()