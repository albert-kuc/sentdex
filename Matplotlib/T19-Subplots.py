""" Source:
    https://pythonprogramming.net/subplot2grid-add_subplot-matplotlib-tutorial/

    Tutorial 19: Subplots
    Only shows the subplot procedure and does not have a solution for overlapping issue
"""

import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()

def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys


# """ Create subplots with add_subplot """
# ax1 = fig.add_subplot(221)  # 2 tall (split y in two), 2 wide (split x in two), plot number 1, top left
# ax2 = fig.add_subplot(222)  # 2 tall (split y in two), 2 wide (split x in two), plot number 2, top right
# ax3 = fig.add_subplot(212)  # 2 tall (split y in two), 1 wide (single x plot), plot number 1, bottom

""" Create subplots with subplot2grid """
ax1 = plt.subplot2grid((6,2), (0,0), rowspan=2, colspan=1)
ax4 = plt.subplot2grid((6,2), (0,1), rowspan=2, colspan=1)
ax2 = plt.subplot2grid((6,1), (2,0), rowspan=3, colspan=1)
ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)
# 1st brackets define the grid split for subplots 6 raws and 2 columns
# 2nd brackets define the position of the subplot (5, 1) row 6 and column 2
# rowspan dna colspan define the height and width of an individual subplot

x, y = create_plots()
ax1.plot(x, y)
x, y = create_plots()
ax2.plot(x, y)
x, y = create_plots()
ax3.plot(x, y)
ax4.plot(x, y)

plt.show()
