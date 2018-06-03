"""
    Image gradients can be used to measure directional intensity,
    and edge detection does exactly what it sounds like: it finds edges!

    https://pythonprogramming.net/canny-edge-detection-gradients-python-opencv-tutorial/
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplation = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    edges = cv2.Canny(frame, 100, 200)

    cv2.imshow('original', frame)
    cv2.imshow('laplation', laplation)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
