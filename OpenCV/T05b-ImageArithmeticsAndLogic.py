import numpy as np
import cv2

# Load images
img1 = cv2.imread("images/3D-Matplotlib.png", 1)
img2 = cv2.imread("images/mainlogo.png", 1)

# Select img1 region to modify based on img2 parameters
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]          # Region of image 1

# Mask from img2
# Starts with initial conversion to grayscale
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# Next to apply threshold (where to apply, what would be the threshold value (over, max), applied inverse here)
# Everything in range 220-255 will be converted to 255 and blow to 0 and then inverted with binary_inv.
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Invisible mask. Bitwise_not(mask) the part where is no mask. (Looks like mask inverted once more)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv', mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Create parts of img1 and img2 for addition
img1_background = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_foreground = cv2.bitwise_and(img2, img2, mask=mask)
cv2.imshow('img1_background', img1_background)
cv2.imshow('img2_foreground', img2_foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Adds img1_bg and img2_fg
dst = cv2.add(img1_background, img2_foreground)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Modify range of img1 with dst
img1[0:rows, 0:cols] = dst

cv2.imshow("res", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
