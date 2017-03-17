#!/usr/bin/python
import sys
from optparse import OptionParser

# A typical usage function
def usage(msg, retval):
  sys.stderr.write("Error: " + msg + "\n")
  sys.exit(retval)

# The option parser will accept short and long arguments.  eg.
# ./opt.py -f /etc/passwd -c ./conf.txt
# or 
# ./opt.py --file /etc/passwd --config-file ./conf.txt
# If you run ./opt.py --help, you'll see the help for the script.

parser = OptionParser()
parser.add_option('-f', '--file', dest='filename', help='file to change', metavar='FILE')
parser.add_option('-c', '--config-file', dest='config_file', help='configuration file', metavar='CONF')

# We basically ignore the args variable in this example.  If you are curious, you can look at:
# http://docs.python.org/library/optparse.html
# to see how it would be used.

(options,args) = parser.parse_args()

# Exit if the options were not given
if not options.filename or not options.config_file:
  usage("Missing option: both filename and config file are required", 2)

# We just print the options out; in your own code, you would actually do something useful with them.
print 'filename ', options.filename
print 'config_file', options.config_file
