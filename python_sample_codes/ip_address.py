#!/usr/bin/python

# To use perl-ish syntax for regular expressions, import the 're' module.
import re
import sys


string='88.45.1.20 - - [13/Oct/2010:20:39:15 -0700] "GET /~smerj/ HTTP/1.1" 200 877 "-" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.10) Gecko/20100914 Firefox/3.6.10 138.23.169.15"'
pattern='\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
result=re.findall(pattern,string)
for match in result:
      print match
      next = sys.stdin.readline()



# Parenthesis introduce grouping.
pattern='(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
result=re.search(pattern,string)
if result:
    print 'first group ', result.group(1), ' second group ', result.group(2)
    next = sys.stdin.readline()
# QUESTION: why does this look weird?  what would you do about it?

# Answer .* is GREEDY.  It will eat as much of the line as it can.  You need to find some 
# way to limit what it consumes.


# Try (1) - put a non-digit character before the second group
pattern='(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*[^\d](\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
result=re.search(pattern,string)
if result:
    print 'try 1: first group ', result.group(1), ' second group ', result.group(2)
    next = sys.stdin.readline()


# Try (2) turn off greedy matching for the '*'
pattern='(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
result=re.search(pattern,string)
if result:
    print 'try 2: first group ', result.group(1), ' second group ', result.group(2)
    next = sys.stdin.readline()


