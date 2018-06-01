import numpy as np
import cv2
# Read image in color
img = cv2.imread("images/bookpage.jpg")

# Apply threshold to image. 12-255 to 255 and else to 0.
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

# Show image in color and threashold
cv2.imshow("image", img)
cv2.imshow("threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert image to grayscale
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

cv2.imshow("image2", grayscaled)
cv2.imshow("threshold2", threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Apply adaptive threshold to grayscaled image
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("gaus", gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()