#!/usr/bin/python

import sys
import csv
import re

oldKey = None

cachedUserValues = None
cachedPostsValues = []


# input data will be csv style and will come in two different formats:
#     user_id, table_type, reputation
#     user_id, table_type, post_id, title, tagnames
# we want to join the forum posts with their author reputation by user_id.
# we will write to standard output the user_id, table identifier, other table details

reader = csv.reader(sys.stdin, delimiter = '\t', quotechar = '"')
writer = csv.writer(sys.stdout, delimiter ='\t', quotechar = '"', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line) < 2:
        continue

    thisKey = line[0]
    type = line[1]
   # print line
    
    if oldKey and thisKey != oldKey:
        for post in cachedPostsValues:
            if cachedUserValues:
                userRating = cachedUserValues[2]
            else:
                userRating = ''
            writer.writerow([post[0], post[2], post[3], post[4], userRating])
        if len(cachedPostsValues) == 0:
            writer.writerow(["", "", "", "", cachedUserValues[2]])

        oldKey = thisKey
        cachedUserValues = None
        cachedPostsValues = []

    oldKey = thisKey
    if type == 'U':
        cachedUserValues = line
    elif type == 'P':
        cachedPostsValues.append(line)

if oldKey:
    for post in cachedPostsValues:
        if cachedUserValues:
            userRating = cachedUserValues[2]
        else:
            userRating = ''
        writer.writerow([post[0], post[2], post[3], post[4], userRating])
    if len(cachedPostsValues) == 0:
        writer.writerow(["", "", "", "", "", cachedUserValues[2]])

