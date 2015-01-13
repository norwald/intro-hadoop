#!/usr/bin/python

import sys

sales_total = 0
sales_counter = 0

# Loop around the data
# It will be in the format key\tval
# We will calculate total sales volume and number per key

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    this_key, this_sale = data_mapped

    sales_total += float(this_sale)
    sales_counter += 1

print sales_total, "\t", sales_counter

