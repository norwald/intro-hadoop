#!/usr/bin/python

import sys

old_key = None
users_list = []

# the input data is the tap delimited tupple thread_id->user_id
# we want to print to stdout the thread_id and list of users who posted in that thread

for line in sys.stdin:
    mapped_data = line.strip().split("\t")
    # skip wrong lines
    if len(mapped_data) != 2:
        continue
    
    this_key, this_val = mapped_data
    
    if old_key and old_key != this_key:
        print "{0}\t{1}".format(old_key, users_list)
        users_list = []

    old_key = this_key
    users_list.append(this_val)

if old_key:
    print "{0}\t{1}".format(old_key, users_list)

