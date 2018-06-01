import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Not BRG any more.
    # hsv [hue sat light]
    lower_orange = np.array([5, 150, 0])
    upper_orange = np.array([55, 255, 255])

    # Mask - 0 or 1 depending on the following. Everything in range is 1.
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    # Result. Applied to frame, where frame is equal to frame and where mask equals mask
    # With bitwise operation every 1's in mask we will show color from the frame
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
