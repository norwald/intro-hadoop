#!/usr/bin/python

import sys
import csv
import re

old_key = None

cached_user_values = None
cached_posts_values = []


# input data will be csv style and will come in two different formats:
#     user_id, table_type, reputation
#     user_id, table_type, post_id, title, tagnames
# we want to join the forum posts with their author reputation by user_id.
# we will write to standard output the user_id, table identifier, other table details

reader = csv.reader(sys.stdin, delimiter = '\t', quotechar = '"')
writer = csv.writer(sys.stdout, delimiter ='\t', quotechar = '"', quoting=csv.QUOTE_ALL)

for line in reader:
    # skip invalid line
    if len(line) < 2:
        continue

    this_key = line[0]
    type = line[1]
    
    # new key group
    if old_key and this_key != old_key:
        for post in cached_posts_values:
            # a user rating exists
            if cached_user_values:
                user_rating = cached_user_values[2]
            else:
                user_rating = ''
            writer.writerow([post[0], post[2], post[3], post[4], user_rating])
        
        # there are no posts for the user
        if len(cached_posts_values) == 0:
            writer.writerow(["", "", "", "", cached_user_values[2]])

        old_key = this_key
        cached_user_values = None
        cached_posts_values = []

    # same key group
    old_key = this_key
    if type == 'U':
        cached_user_values = line
    elif type == 'P':
        cached_posts_values.append(line)

# end of stream
if old_key:
    for post in cached_posts_values:
        if cached_user_values:
            user_rating = cached_user_values[2]
        else:
            user_rating = ''
        writer.writerow([post[0], post[2], post[3], post[4], user_rating])
    if len(cached_posts_values) == 0:
        writer.writerow(["", "", "", "", "", cached_user_values[2]])

