""" Source:
    https://www.youtube.com/watch?v=QyhqzaMiFxk&index=7&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

    Tutorial 7:
    Loading Data from Files
"""

import matplotlib.pyplot as plt
import numpy as np


x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)

plt.plot(x, y, label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph')
plt.legend()
plt.show()
