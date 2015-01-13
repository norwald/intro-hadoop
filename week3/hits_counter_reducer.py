#!/usr/bin/python

import sys

counter = 0
old_key = None

# loop around the data
# it will be in the format key\tval
# we will calculate total occurences per key

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    this_key, this_counter = data_mapped

    if old_key and old_key != this_key:
        print old_key, "\t", counter
        counter = 0

    old_key = this_key
    counter += 1

if old_key != None:
    print old_key, "\t", counter

