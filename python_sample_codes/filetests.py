#!/usr/bin/python

# Import modules that provide specific functionality used later in the script.
import stat
import sys
import os

# Function to print error message to standard error and exit with a nonzero value.
def usage(msg):
  sys.stderr.write('Error: ' +  msg + "\n")
  sys.exit(1)

# Check number of command line arguments.  sys.argv[0] is the name of the program itself,
# so the length of argv is 1 + the number of command line arguments.
if len(sys.argv) != 2:
  usage(sys.argv[0] + ' accepts exactly one command line argument')

# sys.argv[1] is the first command line argument.
file=sys.argv[1]

# File tests.  These are equivalent to tests in Bash.

if not os.path.exists(file):
  usage(file + ' does not exist, we are not performing any further tests on it')

if os.path.isdir(file):
  print file, 'is a directory'

if os.path.islink(file):
  print file, 'is a symbolic link'

if os.path.isfile(file):
  print file, 'is a regular file or symbolic link'

if os.access(file, os.R_OK):
  print file, 'is readable by the current user'

if os.access(file,os.W_OK):
  print file, 'is writable by the current user'

if os.access(file,os.X_OK):
  print file, 'is executable by the current user'
  
# If you have worked with permissions in C, some of this might look familiar.  It's 
# much less convenient than working with permissions in Bash!
# This is true by default for all of the scripting languages (Perl, Python, Ruby).

if os.stat(file).st_mode & stat.S_ISUID:
  print file, 'is setuid'

print 'octal file permissions are', oct(stat.S_IMODE(os.stat(file).st_mode))
