""" Source:
    https://pythonprogramming.net/share-x-axis-sharex-matplotlib-tutorial/

    T23 - Share X Axis, sharex

    Basic copy from T20 final version
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style

import numpy as np
import urllib

""" Import style """
style.use('fast')
# see all styles available:
# print(plt.style.available)

""" Some values defined for moving averages based on T21 """
MA1 = 10
MA2 = 30


""" Two new functions added with T21 """
def moving_average(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas

def high_minus_low(highs, lows):
    return highs-lows

""" converts data to num format for matplotlib """
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
    plt.title(stock)
    plt.ylabel('H-L')
    ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1)
    plt.ylabel('Price')
    ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)
    plt.ylabel('MAvgs')


    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[2:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    """ Copy values from stock_data tuple to variables """
    date, openp, highp, lowp, closep, adj_closep, volume = np.loadtxt(stock_data[:500],
                                                                      # stock_data for last 50 values
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      # converts data to num format for matplotlib
                                                                      converters={0: bytespdate2num('%Y-%m-%d')})

    """ T21 and T22 to plot ax1 """
    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2-1:])

    h_1 = list(map(high_minus_low, highp, lowp))

    ax1.plot_date(date, h_1, '-')
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=5, prune='lower'))

    """ Plot ax2"""
    ax2.plot_date(date, closep, '-', linewidth=0.5, label='Close price')
    ax2.plot_date(date, openp, '-', linewidth=0.5, label='Open price')

    """ T18 Annotation example for last chart value in ax2"""
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    # below we use positive values because the data plots in backward direction
    ax2.annotate(str(closep[1]), (date[1], closep[1]),              # 1st the text, 2nd the location
                 xytext = (date[1]+20, closep[1]+0.5), bbox=bbox_props)

    """ T21 and T22 to plot ax3 """
    ax3.plot(date[-start:], ma1[-start:], linewidth=1)
    ax3.plot(date[-start:], ma2[-start:], linewidth=1)

    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] < ma2[-start:]),
                     facecolors='r', edgecolor='r', alpha=0.5)

    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] > ma2[-start:]),
                     facecolors='b', edgecolor='b', alpha=0.5)

    """ X axis label """

    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))     # set x axis display format
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))                # set x axis number of appearing marks

    # Rotate label
    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)              # tilt angle in brackets but labels are off the screen

    """ Plot parameters """
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.subplots_adjust(left=0.11,           # adjust all parameters
                        bottom=0.24,
                        right=0.92,
                        top=0.90,
                        wspace=0.2,         # wspace and hspace are padding between figures
                        hspace=0)
    plt.show()


graph_data('Sample stock')
