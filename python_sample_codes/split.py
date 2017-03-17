#!/usr/bin/python

import re

# You are already familiar with splitting a string into parts and selecting only
# one "column" using awk.   Python has a simiar facility and can split a string
# based on individual characters or on patterns.

# The pattern we are going to split on
ifs=':'

# Declare a list of logins
logins = []

# Iterate through the password file and append all logins to the list
for line in open('/etc/passwd'):
#  print 'the line is ' + line.rstrip()
  logins.append(re.split(ifs, line)[0])

# Print all the logins  
for login in logins:
  print "login: %s" % (login)

