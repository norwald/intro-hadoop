#!/usr/bin/python

import sys

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want to get the tupple item -> sale cost
# We need to write them out to standard output, separated by a tab

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(item, cost)

