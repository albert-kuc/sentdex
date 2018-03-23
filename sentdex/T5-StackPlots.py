""" Source:
    https://www.youtube.com/watch?v=Z81JW1NTsO8&index=5&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

    Tutorial 5:
    Stack Plots
"""

import matplotlib.pyplot as plt

# Overview activities during a day
days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 7, 5]
eating = [2, 3, 2, 3, 3]
working = [8, 7, 10, 8, 5]
playing = [7, 6, 6, 6, 11]

# Stackplot does not support legend so to display a legend it is required to make it a bit unusual
plt.plot([], [], color='m', label='Sleeping')
plt.plot([], [], color='k', label='Eating')
plt.plot([], [], color='c', label='Working')
plt.plot([], [], color='b', label='Playing')

# below its colors and not color
plt.stackplot(days, sleeping,eating,working,playing, colors=['m', 'k', 'c', 'b'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph')
plt.legend()
plt.show()
