"""
    Overview of some frame filtering options
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Not BRG any more.
    # hsv [hue sat light]
    lower_orange = np.array([35, 80, 0])
    upper_orange = np.array([95, 215, 255])

    # Mask - 0 or 1 depending on the following. Everything in range is 1.
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    # Result. Applied to frame, where frame is equal to frame and where mask equals mask
    # With bitwise operation every 1's in mask we will show color from the frame
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Now, let's apply a simple smoothing, where we do a sort of averaging per block of pixels.
    # In our case, let's do a 15 x 15 square, which means we have 225 total pixels.
    kernel = np.ones((15, 15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)

    blur = cv2.GaussianBlur(res, (15, 15), 0)
    median = cv2.medianBlur(res, 15)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('meadian', median)
    cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
