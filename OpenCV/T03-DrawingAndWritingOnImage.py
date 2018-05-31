"""
    Tutorial for drawing and writing on opened image:
    Line, rectangle, circle, polyline, writing
"""

import numpy as np
import cv2

img = cv2.imread("watch.jpg", 1)    # 1 = cv2.IMREAD_COLOR

# Line (where, start, end, color(BGR), width)
cv2.line(img, (0, 0), (150, 150), (0, 255, 0), 5)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rectangle (where, topleft, bottomright, color, width (negative fill in))
cv2.rectangle(img, (30, 30), (200, 150), (255, 255, 0), 3)

cv2.imshow('image2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Circle (where, center, radius, color, width (negative fill in))
cv2.circle(img, (100, 100), 55, (0, 0, 255), 5)

cv2.imshow('image3', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Polylines
pts = np.array([[10, 5], [20, 40], [50, 15], [70, 10], [100, 50]], np.int32)
# pts = pts.reshape((-1,1,2))   # required based on documentation but not used
# Polylines (where, points, True - connect last to first point
cv2.polylines(img, [pts], True, (0, 255, 255), 3)

cv2.imshow('image4', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Write
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts!', (170, 130), font, 0.5, (200, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image5', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
