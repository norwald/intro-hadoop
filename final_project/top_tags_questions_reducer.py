#!/usr/bin/python

import sys

# the input data is the tab delimited tupple tag->1
# we want to output the ten most common tags

LEN = 10
old_key = None
tag_count = 0 
top_tags = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    # skip wring lines
    if len(data_mapped) != 2:
        continue

    this_key, thi_val = data_mapped
    
    if old_key and old_key != this_key:
        top_tags.append([old_key, tag_count])
        tag_count = 0 

    old_key = this_key
    tag_count += 1

if old_key:
    top_tags.append([old_key, tag_count])

top_tags =sorted(top_tags, key=lambda x: x[1], reverse=True)
for tag in top_tags:
    print  "{0}\t{1}".format(tag[0], tag[1])

