#!/usr/bin/python

import sys
import csv
import re

# input data will be tab delimited.
# node id is column 1, forum post is column 5
# we want to find all forum nodes where a word is found.
# the words should be case insensitive.
# we will write to standard output to the tab separated tupple word -> node id

reader = csv.reader(sys.stdin, delimiter = '\t', quotechar = '"')

#pattern = r'.,!?:;"()<>[]#$=-/'
#print pattern

for line in reader:
    id = line[0]
    post = line[4]
    wordsList = re.split('[\n \.,!\?:;"\(\)<>\[\]#\$=\-/]', post)
    #print wordsList
    for word in wordsList:
         if word != '':
             print "{0}\t{1}".format(word.lower(), id)

