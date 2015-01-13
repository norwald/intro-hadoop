#!/usr/bin/python

import sys

counter = 0
sum = 0 
old_key = None


# Format of each line is:
# weekday\tcost
#
# We want to calculate the average sale per weekday
# We need to write the result to standard output, separated by a tab

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    # skip invalid record
    if len(data_mapped) != 2:
        continue

    this_key, this_cost = data_mapped
    if old_key and this_key != old_key:
        print old_key, "\t", sum/counter
        counter = 0
        sum = 0

    old_key = this_key
    counter += 1
    sum += float(this_cost)

if old_key:
    print old_key, "\t", sum/counter

