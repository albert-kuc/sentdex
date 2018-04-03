import matplotlib.pyplot as plt
import matplotlib.animation as animation        # allow to animate the figure after it has been shown
from matplotlib import style

""" Import style and define figure with subplot """
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

""" The animation function """
def animate(i):
    graph_data = open('example.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))             # float was added because y axis was not in numbering order but appearance
    ax1.clear()                             # clear the plot before printing in the following line
    ax1.plot(xs, ys)


""" 
    We run the animation, putting the animation to the figure (fig), 
    running the animation function of "animate," 
    and then finally we have an interval of 1000, which is 1000 milliseconds, or one second 
"""
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
