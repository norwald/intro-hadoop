#!/usr/bin/python

import sys
from datetime import datetime

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want to get the tupple weekday -> sale cost
# We need to write them out to standard output, separated by a tab

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday, cost)

