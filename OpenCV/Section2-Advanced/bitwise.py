import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

# Bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND', bitwise_and)

# Bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# Bitwise NOT 
bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT for circle', bitwise_not_circle)
bitwise_not_rectangle = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT for rectangle', bitwise_not_rectangle)

cv.waitKey(0)