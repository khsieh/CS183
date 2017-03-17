#!/bin/bash

while read usr; do
    usrname=`echo $usr | awk -F':' '{print $1}';`
    uid=`echo $usr | awk -F':' '{print $3}';`
    group_array=()
    while read grp; do
	group_line=`echo $grp | grep $usrname | awk -F':' '{print $1}';`
	group_array+=($group_line)
    done </etc/group
    printf $usrname" "$uid 
    for i in "${group_array[@]}"
    do
	printf " "$i
    done
    printf '\n'
    
done </etc/passwd

