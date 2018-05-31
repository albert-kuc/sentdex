import numpy as np
import cv2

img1 = cv2.imread("images/3D-Matplotlib.png")
img2 = cv2.imread("images/mainsvmimage.png")

# Addition operation - not much useful
add = img1 + img2
add2 = cv2.add(img1, img2)          # adds all pixel values together

cv2.imshow("add", add)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("add2", add2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Weighted (image1, im1weight%, image2, im2weight%, gamma)
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow("weighted", weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
