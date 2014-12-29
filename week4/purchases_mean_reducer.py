#!/usr/bin/python

import sys

counter = 0
sum = 0 
oldKey = None


# Format of each line is:
# weekday\tcost
#
# We want to calculate the average sale per weekday
# We need to write the result to standard output, separated by a tab

for line in sys.stdin:
    dataMapped = line.strip().split("\t")
    if len(dataMapped) != 2:
        continue

    thisKey, thisCost = dataMapped
    if oldKey and thisKey != oldKey:
        print oldKey, "\t", sum/counter
        oldKey = thisKey
        counter = 0
        sum = 0

    oldKey = thisKey
    counter += 1
    sum += float(thisCost)

if oldKey:
    print oldKey, "\t", sum/counter

