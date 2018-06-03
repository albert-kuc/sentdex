import cv2
import numpy as np

img = cv2.imread("images\\opencv-corner-detection-sample.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# image, max corners to detect, quality, and minimum distance between corners.
# The aliasing issues we have here will allow for many corners to be found, so we put a limit on it
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

# Now we iterate through each corner, making a circle at each point that we think is a corner.
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
