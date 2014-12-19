#!/usr/bin/python

import sys

salesTotal = 0
salesCounter = 0

# Loop around the data
# It will be in the format key\tval
# We will calculate total sales volume and number per key

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    salesTotal += float(thisSale)
    salesCounter += 1

print salesTotal, "\t", salesCounter

