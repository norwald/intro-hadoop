#!/usr/bin/python

import sys

sales_max = 0
old_key = None

# Loop around the data
# It will be in the format key\tval
# We will calculate max sales per key

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    this_key, this_sale = data_mapped

    if old_key and old_key != this_key:
        print old_key, "\t", sales_max
        sales_max = 0

    old_key = this_key
    if float(this_sale) > float(sales_max):
        sales_max = this_sale

if old_key != None:
    print old_key, "\t", sales_max

