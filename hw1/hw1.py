#!/usr/bin/python

import sys

if len(sys.argv) > 1:
    for f in sys.argv[1:]:
        with open(f, 'r') as content:
            print content.read()

