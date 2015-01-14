#!/usr/bin/python

import csv
import sys

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
# we want to output the tab separated tupple tagname->1

reader = csv.reader(sys.stdin, delimiter ='\t', quotechar = '"')

for line in reader:
    tagnames = line[2]
    # skip non-question nodes
    if line[5] != "question":
        continue
    # skip missing tagnames
    if len(tagnames) == 0:
        continue
    # skip header row
    if tagnames == "tagnames":
        continue
    
    tags = tagnames.strip().split()
    for tag in tags:
        print "{0}\t{1}".format(tag, 1)

