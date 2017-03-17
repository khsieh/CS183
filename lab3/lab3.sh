#!/bin/bash

echo "Find all files in /bin, /sbin, /usr/bin, and /usr/sbin that are setuid and owned by root."
find /bin -xdev \( -perm -4000 \) -type f -print0 | grep root | xargs -0 ls -l
find /sbin -xdev \( -perm -4000 \) -type f -print0 | grep root | xargs -0 ls -l
find /usr/bin -xdev \( -perm -4000 \) -type f -print0 | grep root | xargs -0 ls -l
find /usr/sbin -xdev \( -perm -4000 \) -type f -print0 | grep root | xargs -0 ls -l

read -p "Hit ENTER to conitnue"

echo "Find all files in /var that have changed in the last 20 minutes."
find /var -type f -mmin -20 -print
read -p "Hit ENTER to conitnue"

echo "Find all files in /var that are regular files of zero length."
find /var -type f -empty -print
read -p "Hit ENTER to continue"

echo "Find all files in /dev that are not regular files and also not directories."
find /dev -not -type f -not -type d -exec ls -alu {} \;
read -p "Hit ENTER to continue"

echo "Find all directories in /home that are not owned by root" #change permission to 711
find /home -type d -not -user root -exec chmod u+wrx,g+x,o+x {} \;
read -p "Hit ENTER to continue"

echo "Find all regular files in /home that are not owned by root." #change permission to 755
find /home -type f -not -user root -exec chmod u+wrx,g+rx,o+rx {} \;
read -p "Hit ENTER to continue"

echo "Find all files (of all types) in /etc that have changed in the last 5 days."
find /etc -mtime 5
read -p "Hit ENTER to continue"
