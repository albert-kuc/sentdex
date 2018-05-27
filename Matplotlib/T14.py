""" Source:
    https://www.youtube.com/watch?v=S5Dn1HjBPA4

    Tutorial 14:

    This tutorial was supposed to create candlestick graphs but matplotlib library does not work anymore
    Instead T10 file is extended with few additional modifications from T12-T14
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

import numpy as np
import urllib

""" converts data to num format for matplotlib """
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data():

    fig = plt.figure()              # to modify a figure we need to reference the figure first
    # One subplot added in following line
    ax1 = plt.subplot2grid((1, 1),  # 1st tuple - shape of the grid -> 1 by 1
                           (0, 0))  # 2nd typle - starting point of this plot
    """ As we got ax1 below we will plot it and not plt """


    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[2:]:
        split_line = line.split(',')
        if len(split_line) == 7:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, openp, highp, lowp, closep, adj_closep, volume = np.loadtxt(stock_data,
                                                                      delimiter=',',
                                                                      unpack=True,
                                                                      # converts data to num format for matplotlib
                                                                      converters={0: bytespdate2num('%Y-%m-%d')})
    """ Plot """
    ax1.plot_date(date, closep, '-', linewidth=0.5, label='Price')

    # ax1.fill_between(date,
    #                  closep,
    #                  200,                      # set fill starting y position
    #                  alpha=0.3)                # set fill transparency

    # Same as above but divided into green and red area
    ax1.fill_between(date, closep, closep[0], where=(closep > closep[0]), facecolor='g', alpha=0.5)
    ax1.fill_between(date, closep, closep[0], where=(closep < closep[0]), facecolor='r', alpha=0.5)
    # Create empty plot to add labels for green and red area
    ax1.plot([], [], linewidth=3, label='gain', color='g')
    ax1.plot([], [], linewidth=3, label='loss', color='r')

    """ Grid """
    # ax1.grid(True, color='g')               # adds grid to figure

    """ X axis label """
    # Rotate label
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)              # tilt angle in brackets but labels are off the screen

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))     # set x axis display format
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))                # set x axis number of appearing marks

    """ Y axis label """
    ax1.set_yticks([0, 120, 240, 360, 400, 500, 550, 660, 720])

    """ Plot parameters """
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting graph')
    plt.legend()
    plt.subplots_adjust(left=0.09,           # adjust all parameters
                        bottom=0.20,
                        right=0.94,
                        top=0.90,
                        wspace=0.2,         # wspace and hspace are padding between figures
                        hspace=0)
    plt.show()


graph_data()
