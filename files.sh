#!/bin/bash

bin=`find /usr/bin -xdev \( -perm -4000 \) -type f -print0 | grep root | xargs -0 ls -l;`
echo $bin
read -p "Hit ENTER to conitnue"
