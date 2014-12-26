#!/usr/bin/python

import sys

keyList = set()
oldKey = None

# loop around the data
# it will be in the format key\tval
# we will form sorted list of all vals for a given key

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisVal = data_mapped
    if thisVal == 'id':
        continue
    
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", sorted(keyList, key=int)
        oldKey = thisKey;
        keyList = set()

    oldKey = thisKey
    keyList.add(thisVal)

if oldKey != None:
    print oldKey, "\t", sorted(keyList, key = int)

