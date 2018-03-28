""" Source:
    https://www.youtube.com/watch?v=IbUa1tTT-7k&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF&index=8

    Tutorial 8 & 9:
    Getting data from Yahoo finances API, replaced with other link as yahoo API's are not available anymore
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
    plt.plot_date(date, closep, '-', label='Price')

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting graph')
    plt.legend()
    plt.show()


graph_data()
