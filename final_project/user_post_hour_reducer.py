#!/usr/bin/python

import sys

# the input data is will be a tab delimited tupple user_id->hour
# we want to find the most common hour for each user_id

def find_max_vals_indeces(values_list):
    max_val = 0
    max_vals_indeces = []
    for index in range(len(values_list)):
        if values_list[index] > max_val:
            max_val = values_list[index]
            max_vals_indeces = []
            max_vals_indeces.append(index)
        elif values_list[index] == max_val:
            max_vals_indeces.append(index)
    return max_vals_indeces

old_key = None
hours_freq = [0] * 24

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    # skip wring lines
    if len(data_mapped) != 2:
        continue
    this_key, this_hour = data_mapped    

    if old_key and old_key != this_key:
        for hour in  find_max_vals_indeces(hours_freq):
            print "{0}\t{1}".format(old_key, hour)
        
        old_key = this_key
        hours_freq = [0] * 24

    old_key = this_key
    hours_freq[int(this_hour)] += 1

if old_key:
    for hour in  find_max_vals_indeces(hours_freq):
        print "{0}\t{1}".format(old_key, hour)  

