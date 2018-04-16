"""
    Parsing data:
    1. Locate all files in specified directory.
    2. Pulling data from file in specified location.

    https://pythonprogramming.net/getting-data-machine-learning/
"""

import pandas as pd
import os
import time
from datetime import datetime

path = "D:/Python/intraQuarter"


def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+"/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]     # create a path list to all folders
    print(stock_list)

    for each_dir in stock_list[1:]:                     # [1:] first stock list is initial pattern
        each_file = os.listdir(each_dir)
        if len(each_file) > 0:
            for file in each_file:

                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')   # save file name as date value

                unix_time = time.mktime(date_stamp.timetuple())
                print(date_stamp, unix_time)
                time.sleep(5)


Key_Stats()
