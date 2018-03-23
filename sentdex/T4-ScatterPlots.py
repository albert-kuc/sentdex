""" Source:
    https://www.youtube.com/watch?v=WbTOutpwPHs&index=4&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

    Tutorial 4:
    Scatter Plots
"""

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [5,2,6,3,7,8,9,2]

plt.scatter(x, y, label='skitscat', color='k', marker='*', s=100)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph')
plt.legend()
plt.show()