import numpy as np
import cv2

img = cv2.imread("images/watch.jpg", cv2.IMREAD_COLOR)

# Print certain characteristic of image
print(img.shape)
print(img.size)
print(img.dtype)

# Check color of a pixel location
px = img[55, 55]
print(px)

# Modify a pixel
img[55, 55] = [255, 255, 255]
px = img[55, 55]
print(px)

# Region of Image - subimage of image
roi = img[100:150, 100:150]
# print(roi)

# modifying ROI
img[100:150, 100:150] = [255, 255, 255]
#print(roi)

# Copy and paste part of image
watchface = img[37:111, 107:194]
img[0:74, 0:87] = watchface

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
