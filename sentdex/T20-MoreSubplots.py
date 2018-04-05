""" Source:
    https://pythonprogramming.net/implementing-subplots-matplotlib-tutorial/

    Tutorial 20: Implementing Subplots
    Tutorial 21: Adding more indicator data

    Start with copy from T15 and adds new subplots at top and bottom
    T21 adds data to new subplots
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


def graph_data():

    fig = plt.figure()
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
    plt.title('stock')
    ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1)
    plt.xlabel('Date')
    plt.ylabel('Price')
    ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)


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
    date, openp, highp, lowp, closep, adj_closep, volume = np.loadtxt(stock_data[:50],
                                                                      # stock_data for last 50 values
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      # converts data to num format for matplotlib
                                                                      converters={0: bytespdate2num('%Y-%m-%d')})

    """ T21 to plot ax1 and ax3 """
    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2-1:])

    h_1 = list(map(high_minus_low, highp, lowp))

    ax1.plot_date(date, h_1, '-')
    ax3.plot(date[-start:], ma1[-start:])
    ax3.plot(date[-start:], ma2[-start:])

    """ Plot """
    ax2.plot_date(date, closep, '-', linewidth=0.5, label='Close price')
    ax2.plot_date(date, openp, '-', linewidth=0.5, label='Open price')

    """ Fill between for plotting areas below or above certain value in color"""
    # ax1.fill_between(date,
    #                  closep,
    #                  200,                      # set fill starting y position
    #                  alpha=0.3)                # set fill transparency

    # Same as above but divided into green and red area
    # ax1.fill_between(date, closep, closep[0], where=(closep > closep[0]), facecolor='g', alpha=0.5)
    # ax1.fill_between(date, closep, closep[0], where=(closep < closep[0]), facecolor='r', alpha=0.5)
    # Create empty plot to add labels for green and red area
    # ax1.plot([], [], linewidth=3, label='gain', color='g')
    # ax1.plot([], [], linewidth=3, label='loss', color='r')

    """ Grid """
    # ax1.grid(True, color='g')               # adds grid to figure

    """ X axis label """
    # Rotate label
    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)              # tilt angle in brackets but labels are off the screen

    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))     # set x axis display format
    ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))                # set x axis number of appearing marks

    """ Y axis label """
    # Fix specified values to Y axis
    # ax1.set_yticks([0, 120, 240, 360, 400, 500, 550, 660, 720])

    """ T17 Annotation example with arrow"""
    ax2.annotate('Bad News!',(date[15],openp[15]),                  # pointed location based on variables
                 xytext=(.605, .4), textcoords='axes fraction',     # xytexy (Xaxis, Yaxis in percentage
                 arrowprops=dict(facecolor='grey', color='grey'))   # warning is caused by "color"s property

    """ T18 Annotation example for last chart value"""
    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=1)
    # below we use positive values because the data plots in backward direction
    ax2.annotate(str(closep[1]), (date[1], closep[1]),              # 1st the text, 2nd the location
                 xytext = (date[1]+2.5, closep[1]+0.5), bbox=bbox_props)

    """ Plot parameters """
    plt.xlabel('Date')
    plt.ylabel('Price')
    # plt.title('Interesting graph')         # title defined on top because her will be attached to latest subplot
    # plt.legend()
    plt.subplots_adjust(left=0.11,           # adjust all parameters
                        bottom=0.24,
                        right=0.92,
                        top=0.90,
                        wspace=0.2,         # wspace and hspace are padding between figures
                        hspace=0)
    plt.show()


graph_data()
