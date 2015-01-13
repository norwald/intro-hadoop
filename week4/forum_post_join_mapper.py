#!/usr/bin/python

import sys
import csv
import re

# input data will be csv style and will come from two different tables: ForumPosts and Users
# format of ForumPosts table:
#    post_id is column 1, title - column 2, tagnames - column 3, author_id - column 4
# format of Users table:
#    user_ptr_id is column 1, reputaion - column 2 
# we want to join the forum posts with their author reputation by user_id.
# we will write to standard output the user_id, table identifier, other table details

reader = csv.reader(sys.stdin, delimiter = '\t', quotechar = '"')
writer = csv.writer(sys.stdout, delimiter ='\t', quotechar = '"', quoting=csv.QUOTE_ALL)

for line in reader:
    id = line[0]
    # skip header row
    if id == "user_ptr_id" or line[3] == "author_id":
        continue
    # the line comes from the Users table
    if len(line) == 5 and line[1]:
        writer.writerow([id, 'U', line[1]])
    # line comes from the ForumPosts table
    else:
        writer.writerow([line[3], 'P', id, line[1], line[2]])

