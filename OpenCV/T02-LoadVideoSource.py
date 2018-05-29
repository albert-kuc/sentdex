import cv2
import numpy as np

# load video, change 0 if multiple cameras in use
cap = cv2.VideoCapture(0)
# output file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 10.0, (640, 480))

while True:
    # ret (return - True/False) and frame
    ret, frame = cap.read()

    # Defines video frame in grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out.write(frame)
    # Display video frame
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    # this statement runs once per frame and if we get a key, and that key is q then we will exit while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# releases camera
cap.release()
out.release()

cv2.destroyAllWindows()
