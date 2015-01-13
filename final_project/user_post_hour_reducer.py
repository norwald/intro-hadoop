#!/usr/bin/python

import sys

# the input data is will be a tab delimited tupple user_id->hour
# we want to find the most common hour for each user_id

# function returning indeces of the most max values in the list
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

def print_result(key, hours_list):
    for hour in  find_max_vals_indeces(hours_list):
        print "{0}\t{1}".format(key, hour)

old_key = None
hours_freq = [0] * 24 # used to store hour frequences

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    # skip wrong lines
    if len(data_mapped) != 2:
        continue
    this_key, this_hour = data_mapped    

    if old_key and old_key != this_key:
        print_result(old_key, hours_freq)
        hours_freq = [0] * 24

    old_key = this_key
    hours_freq[int(this_hour)] += 1

if old_key:
    print_result(old_key, hours_freq)  

