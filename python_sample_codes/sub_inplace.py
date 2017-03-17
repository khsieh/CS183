#!/usr/bin/python

import re
import sys
import fileinput

# Replace all pound sign comments in a file given as the command line argument.
# Makes a backup file when doing so.
# This illustrates use of a library.  The arguments to calling a function from a 
# library can be arbitrarily complex - it's good to read the documentation and 
# to TEST your understanding.

# Note: no error checking!

pattern='#.*$'
for line in fileinput.FileInput(sys.argv[1], inplace=1, backup='.bak'):
  line=line.rstrip()
  res=re.sub(pattern,'',line)
  if len(res) != 0: 
    print res

