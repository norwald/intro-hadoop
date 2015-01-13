#!/usr/bin/python

import sys
import csv

# the input data is a tab delimited tsv file
# the columns are:
#    "id": id of the node
#    "title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
#    "tagnames": space separated list of tags
#    "author_id": id of the author
#    "body": content of the post
#    "node_type": type of the node, either "question", "answer" or "comment"
#    "parent_id": node under which the post is located, will be empty for "questions"
#    "abs_parent_id": top node where the post is located
#    "added_at": date added
#
# we want to output the tab separated tupple author_id->hour(added_at)

def get_hour(date_string):
    return date_string[11:13]

reader = csv.reader(sys.stdin, delimiter ='\t', quotechar = '"')

for line in reader:
    author = line[3]
    # skip column header
    if author == "author_id":
        continue
    
    hour = get_hour(line[8])
    print "{0}\t{1}".format(author, hour)

