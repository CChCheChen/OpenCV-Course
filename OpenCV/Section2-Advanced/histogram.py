import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Lady Gray', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)

# ---------- GrayScale Histogram ---------- 
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


# ----------  GrayScale Histogram with mask ---------- 
mask_circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2 - 50), 100, 255, -1)
masked_img_gray = cv.bitwise_and(gray, gray, mask=mask_circle)
# cv.imshow('Lady Gray masked', masked_img_gray)

# gray_hist_mask = cv.calcHist([gray], [0], masked_img_gray, [256], [0,256])
# plt.figure()
# plt.title('Grayscale Histogram with mask')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist_mask)
# plt.xlim([0,256])
# plt.show()

# ----------  Color/RBG Histogram ---------- 
# colors = ('b', 'g', 'r')
# plt.figure()
# plt.title('Color Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# for i,col in enumerate(colors):
#     hist = cv.calcHist([img], [i], None, [256], [0,256])
#     plt.plot(hist, color=col)
#     plt.xlim([0,256])
# plt.show()

# ----------  Color/RBG Histogram with mask---------- 
mask_rectangle= cv.rectangle(blank.copy(), (img.shape[1]//4, img.shape[0]//4), (3*(img.shape[1]//4), 3*(img.shape[0]//4)), 255, -1)
masked_img = cv.bitwise_and(img, img, mask=mask_rectangle)
cv.imshow('Lady masked', masked_img)

colors = ('b', 'g', 'r')
plt.figure()
plt.title('Color Histogram with mask')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask_rectangle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)