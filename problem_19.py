"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import numpy as np
# Because 1900 is not a leap year, Jan 1, 1901 is a tuesday
day = 2
num_suns = 0
years = np.arange(1901, 2001)
for year in years:
    if year % 4 == 0:
        for days in [31,29,31,30,31,30,31,31,30,31,30,31]:
            day += days
            day %= 7
            if day == 0:
                num_suns += 1
    else:
        for days in [31,28,31,30,31,30,31,31,30,31,30,31]:
            day += days
            day %= 7
            if day == 0:
                num_suns += 1
print(num_suns)
