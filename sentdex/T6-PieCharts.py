""" Source:
    https://www.youtube.com/watch?v=Oh2Dkkswy30&index=6&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

    Tutorial 6:
    Pie Charts
"""

import matplotlib.pyplot as plt

# Overview activities during a day
days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 7, 5]
eating = [2, 3, 2, 3, 3]
working = [8, 7, 10, 8, 5]
playing = [7, 6, 6, 6, 11]

slices = [5, 3, 5, 11]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,              # changes starting angle of chart, and runs counterclockwise
        shadow=True,                # adds background sliceÁ
        explode=(0, 0.1, 0, 0),     # takes out eating slice from chart
        autopct='%1.1f%%')          # adds percentage to chart

#plt.xlabel('x')
#plt.ylabel('y')
plt.title('Interesting graph')
#plt.legend()
plt.show()
