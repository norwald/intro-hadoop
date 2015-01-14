#!/usr/bin/python

import sys
import csv
import re

old_key = None

cached_user_values = None
cached_posts_values = []


# input data will be csv style and will come in two different formats:
#     user_id, table_type, user_rating
#     user_id, table_type, post_id, title, tagnames
# we want to join the forum posts with their author reputation by user_id.
# we will write to standard output the user_id, table identifier, other table details

def print_results(user_values, posts_values):
   # the user has no posts 
   if len(posts_values) == 0:
       user_rating = user_values[2] 
       writer.writerow(["", "", "", "", user_rating])
   else:
       for post in posts_values:
           # a user rating exists
           if user_values:
               user_rating = user_values[2]
           else:
               user_rating = ''
           user_id, post_id, title, tagnames = [post[index] for index in [0, 2, 3, 4]]
           writer.writerow([user_id, post_id, title, tagnames, user_rating])   

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
        print_results(cached_user_values, cached_posts_values)
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
    print_results(cached_user_values, cached_posts_values)

