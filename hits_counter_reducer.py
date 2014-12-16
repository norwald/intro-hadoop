#!/usr/bin/python

import sys

counter = 0
oldKey = None

# loop around the data
# it will be in the format key\tval
# we will calculate total occurences per key

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCounter = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", counter
        oldKey = thisKey;
        counter = 0

    oldKey = thisKey
    counter += 1

if oldKey != None:
    print oldKey, "\t", counter

