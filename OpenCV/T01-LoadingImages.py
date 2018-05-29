import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
# IMREAD_GRAYSCALE = 0
# IMREAD_UNCHANGED = -1

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Image show in matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([40, 100], [80, 100], 'c')
# plt.show()

cv2.imwrite('watchgray.jpg', img)