#!/usr/bin/python

import sys

sum = 0 
oldKey = None


# Format of each line is:
# weekday\tcost
#
# We want to calculate the tota sales per weekday
# We need to write the result to standard output, separated by a tab

for line in sys.stdin:
    dataMapped = line.strip().split("\t")
    if len(dataMapped) != 2:
        continue

    thisKey, thisCost = dataMapped
    if oldKey and thisKey != oldKey:
        print oldKey, "\t", sum
        oldKey = thisKey
        sum = 0

    oldKey = thisKey
    sum += float(thisCost)

if oldKey:
    print oldKey, "\t", sum

