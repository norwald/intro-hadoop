#!/usr/bin/python

import sys

sum = 0 
old_key = None


# Format of each line is:
# weekday\tcost
#
# We want to calculate the tota sales per weekday
# We need to write the result to standard output, separated by a tab

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    # skip invalid line
    if len(data_mapped) != 2:
        continue

    this_key, this_cost = data_mapped
    if old_key and this_key != old_key:
        print old_key, "\t", sum
        old_key = this_key
        sum = 0

    old_key = this_key
    sum += float(this_cost)

if old_key:
    print old_key, "\t", sum

