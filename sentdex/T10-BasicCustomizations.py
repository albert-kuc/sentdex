""" Source:
    https://www.youtube.com/watch?v=cLNOADl17b4&index=10&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

    Tutorial 10:
    Basic customizations, rotating labels
"""

import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates


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
    """ As we got ax1 we will plot it and not plt """


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
    ax1.plot_date(date, closep, '-', label='Price')
    # Rotate label
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)              # tilt angle in brackets but labels are off the screen
    ax1.grid(True, color='g')                          # adds grid to figure

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
