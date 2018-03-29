""" Source:
    https://www.youtube.com/watch?v=aRQxMYoCOuI&index=11&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF

    Tutorial 11:
    Handling Unix Time
"""

import datetime as dt
import time
import numpy as np

example = time.time()
print(example)                                          # print current unix time

print(dt.datetime.fromtimestamp(example))               # print current time

dateconv = np.vectorize(dt.datetime.fromtimestamp)      # convert unix time
date = dateconv(example)

print(date)
