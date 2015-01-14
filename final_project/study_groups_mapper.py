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
# we want to output the tab separated tupple question_id->users_id (who posted in the thread)

reader = csv.reader(sys.stdin, delimiter ='\t', quotechar = '"')

for line in reader:
    # skip head row
    if line[0] == "id":
        continue
    post_type = line[5]
    if post_type == "question":
        thread_id = line[0]
    else:
        thread_id = line[7]
    
    user_id = line[3]

    print "{0}\t{1}".format(thread_id, user_id)

