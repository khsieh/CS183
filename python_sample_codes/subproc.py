#!/usr/bin/python

"""
Runs a shell command given as the command line argument as a subprocess. 
It prints out:
standard output of the shell command
standard error of the shell command
return value of the shell command
"""

import subprocess 
import string
import re
import sys

command=string.join(sys.argv[1:])

# If you want to break this down by parts and see what each one does, take a look at the documentation
# for subprocess:
# http://docs.python.org/library/subprocess.html 

proc=subprocess.Popen([command], shell=True, stdin=sys.stdin, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout,stderr=proc.communicate()

# All of standard output is returned as a single string with embedded newline.  If you want to process it one line
# at at time, you have to tokenize on newlines.
lines = re.split('\n', stdout.rstrip())
for line in lines:
  print 'stdout: ', line

# Same for standard error
lines = re.split('\n', stderr.rstrip())
for line in lines:
  print 'stderr: ', line

# Print the return value of the command
print 'return value:', proc.returncode
