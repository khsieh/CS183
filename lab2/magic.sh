#!/bin/bash

find /usr/src/* -name "*.h" -print0 | xargs -0 cat | grep -i magic | wc -l | awk '{print $1}'

