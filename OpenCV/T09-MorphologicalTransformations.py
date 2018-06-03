"""
    Overview of Morphological Transformations to remove white noise or noise from filters

    https://pythonprogramming.net/morphological-transformation-python-opencv-tutorial/
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Not BRG any more.
    # hsv [hue sat light]
    lower_orange = np.array([3, 160, 0])
    upper_orange = np.array([14, 255, 255])

    # Mask - 0 or 1 depending on the following. Everything in range is 1.
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    # Result. Applied to frame, where frame is equal to frame and where mask equals mask
    # With bitwise operation every 1's in mask we will show color from the frame
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Erosion and dilation
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    # Opening and Closing
    # False positives are noises in background, and false negatives are noises in object
    # Opening to remove false positives
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
