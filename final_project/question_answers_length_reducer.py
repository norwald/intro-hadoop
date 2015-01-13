#!/usr/bin/python

import sys

# the data will be in the format id\tnode_type\body_length
# we want to find the length of each question and the average length of its answers
# we will print to stdout the tripple: id, length of question, average length of answers

old_key = None
question_len = 0
answers_tot_len = 0
answers_count = 0

for line in sys.stdin:
    mapped_data = line.strip().split("\t")
    # skip wrong line
    if len(mapped_data) != 3:
       continue
    
    this_key, this_code, this_len = mapped_data
    
    if old_key and old_key != this_key:
        if answers_count > 0:
            average_len = float(answers_tot_len / answers_count)
        else:
            average_len = 0
        print "{0}\t{1}\t{2}".format(old_key, question_len, average_len)
        question_len = 0
        answers_tot_len = 0
        answers_count = 0

    old_key = this_key
    if this_code == "Q":
        question_len = int(this_len)
    if this_code == "A":
        answers_tot_len += float(this_len)
        answers_count += 1

if old_key:
    if answers_count > 0:
        average_len = float(answers_tot_len / answers_count)
    else:
        average_len = 0
    print "{0}\t{1}\t{2}".format(old_key, question_len, average_len)

