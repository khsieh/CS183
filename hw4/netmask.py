#!/usr/bin/python

import sys


bits = sys.argv[1]

host_bits = 32 - int(bits)
total_addr = 2**host_bits
usable_addr = total_addr - 2

print "address: " + str(total_addr) + " usable: " + str(usable_addr) + " netmask: " 
