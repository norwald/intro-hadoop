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
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_key, this_cost = data_mapped
    if oldKey and thisKey != oldKey:
        print oldKey, "\t", sum/counter
        oldKey = thisKey
        counter = 0
        mean = 0

    oldKey = thisKey
    counter += 1
    mean += this_cost

if oldKey:
    print oldKey, "\t", sum/counter

