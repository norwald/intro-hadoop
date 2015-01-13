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
# we want to output the tab separated tripple: id of parent node, type of node, length of body

reader = csv.reader(sys.stdin, delimiter ='\t', quotechar = '"')

for line in reader:
    node_type = line[5]    
    if node_type == "question":
        key = line[0]
        tripple_code = "Q"
    elif node_type == "answer":
        key = line[6]
        tripple_code = "A"
    else:
        continue
    
    body_len = len(line[4])
    print "{0}\t{1}\t{2}".format(key, tripple_code, body_len)

