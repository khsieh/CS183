#!/usr/bin/python

import re
import sys

# Let's do something fun: read from standard input and strip all # style comments 
# out of the input using regular expression substitution.

# You'd run this script similar to the following:
# cat somefile_with_embedded_comments.c | ./sub.py
pattern='#.*$'
for line in sys.__stdin__:
  line=line.rstrip()
  res=re.sub(pattern,'',line)
  if len(res) != 0: 
    print res

