#!/usr/bin/python

# Recurses through a directory structure with a base given by the first
# command line argument.
# Does not do any error checking on that argument!

import os
import sys

starting_location=sys.argv[1]
for directory, subdirs, files in os.walk(starting_location):
  for file in files:
    print 'the filename is:', file
    print 'the directory the file is in:', directory
    print 'the (potentially relative) path to the file is:', os.path.join(directory, file) 
    print 'the absolute path to the file is:', os.path.abspath(os.path.join(directory, file)), "\n" 
