"""
    GrabCut Foreground Extraction
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images\\opencv-python-foreground-extraction-tutorial.jpg")
mask = np.zeros(img.shape[:2], np.uint8)

# Background and foreground model
bgModel = np.zeros((1, 65), np.float64)
fgModel = np.zeros((1, 65), np.float64)

# rect = (start_x, start_y, width, height)
rect = (50, 50, 300, 300)

# GrabCut parameters
# First the input image, then the mask, then the rectangle for our main object, the background model, foreground model,
# the amount of iterations to run, and what mode you are using
cv2.grabCut(img, mask, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)

# From here, the mask is changed so that all 0 and 2 pixels are converted to the background, where the 1 and 3 pixels
# are now the foreground. From here, we multiply with the input image, and we get our final result
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img*mask2[:, :, np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()
