"""
    Simple Support Vector Machine (SVM) example with character recognition

    https://pythonprogramming.net/support-vector-machine-svm-example-tutorial-scikit-learn-python/
"""

import matplotlib.pyplot as plt

from sklearn import datasets        # sample dataset, which contains one set that has number recognition data
from sklearn import svm             # Support Vector Machine

digits = datasets.load_digits()     # variable, which is the loaded digit dataset

# print(digits.data)
# print(digits.target)

clf = svm.SVC(gamma=0.001, C=100)   # classifier; note when gamma increased to 0.1 the result is incorrect

print(len(digits.data))

X, y = digits.data[:-10], digits.target[:-10]
# This loads in all but the last 10 data points, so we can use all of these for training.
# Then, we can use the last 10 data points for testing

# Train machine:
clf.fit(X, y)

# Test and print recognised value:
print(clf.predict(digits.data[[-71]]))

# Shows an image of the number in question
plt.imshow(digits.images[-71], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
