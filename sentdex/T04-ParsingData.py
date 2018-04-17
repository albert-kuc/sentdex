"""
    Parsing data:
    4.1. Locate all files in specified directory.
    4.2. Pulling datetime and unix time from file in specified location.
    5.1. Read every file in each directory
    5.2. Strip file data to specified value with source.split
    6.1. Implement DataFrame from Pandas
    6.2. Try if value exists and append to DataFrame dictionary
    6.3. Save as csv

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
    # print(stock_list)
    df = pd.DataFrame(columns = ['Date', 'Unix', 'Ticker', 'DE Ratio'])     # df - data frame
    for each_dir in stock_list[1:]:                     # [1:] first stock list is initial pattern
        each_file = os.listdir(each_dir)
        ticker = each_dir.split('\\')[1]                # ticker is the stock folder name containing files
        if len(each_file) > 0:                          # ignore empty files
            for file in each_file:

                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')   # save file name as date value

                unix_time = time.mktime(date_stamp.timetuple())
                print(date_stamp, unix_time)
                full_file_path = each_dir+'/'+file      # creates path to all files
                print(full_file_path)
                source = open(full_file_path, 'r').read()   # use urllib urlopen for url link
                # print(source)

                """
                    Source split: 
                    First define the part of code used for split. 
                    [1] means to leave everything from first following element on the right.
                    Second split element with [0] defines to remove everything including element defined for split.
                    
                    Try if value exist, if not then pass
                    We attempt to convert value to a float, if not we hit exception and it will just pass.
                """
                try:
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    df = df.append({'Date':date_stamp,'Unix':unix_time,'Ticker':ticker,'DE Ratio':value,},
                                   ignore_index=True)
                except Exception as e:
                    pass

    save = gather.replace(' ','').replace(')','').replace('(','').replace('/','')+('.csv')
    print(save)
    df.to_csv(save  )


Key_Stats()
