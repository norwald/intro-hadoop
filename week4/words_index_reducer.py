#!/usr/bin/python

import sys

key_list = set()
old_key = None

# loop around the data
# it will be in the format key\tval
# we will form sorted list of all vals for a given key

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    this_key, this_val = data_mapped
    if this_val == 'id':
        continue
    
    if old_key and old_key != this_key:
        print old_key, "\t", sorted(key_list, key=int)
        key_list = set()

    old_key = this_key
    key_list.add(this_val)

if old_key != None:
    print old_key, "\t", sorted(key_list, key=int)

