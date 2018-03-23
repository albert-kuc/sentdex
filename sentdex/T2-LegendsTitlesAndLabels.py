""" Source:
    https://www.youtube.com/watch?v=aCULcv_IQYw&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF&index=2

    Tutorial 2:
    Legends Titles and Labels
"""

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 6]

x2 = [1, 2, 3]
y2 = [10, 11, 7]

plt.plot(x, y, label='First line')
plt.plot(x2, y2, label='Second line')
plt.xlabel('Plot number')
plt.ylabel('Important var')

plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()