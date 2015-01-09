#!/usr/bin/python

import sys
import csv
import re

# input data will be csv style and will come in two different formats:
#     user_id, table_type, reputation
#     user_id, title, tagnames, author_id
# we want to join the forum posts with their author reputation by user_id.
# we will write to standard output the user_id, table identifier, other table details

reader = csv.reader(sys.stdin, delimiter = '\t', quotechar = '"')
writer = csv.writer(sys.stdout, delimiter ='\t', quotechar = '"', quoting=csv.QUOTE_ALL)

for line in reader:
    id = line[0]
    # the line comes from the Users table
    if len(line) == 5 and line[1]:
        writer.writerow([id, 'U', line[1]])
    # line comes from the ForumPosts table
    else:
        writer.writerow([id, 'P', line[1], line[2], line[3]])

