#!/bin/bash
#kevin hsieh
#861054367

#short description of what they do in general 
#one or more examples

#dd
#Convert and copy a file, usually used for formatting a file. 
#Create a img file of hard drive at /dev/sda 
dd if=/dev/sda of=~/disk1.img

#find
#Search for files in a directory hierachy 
#Look for a specific file given a fileanme
find -name "hw2.sh"

#file
#Determine file type, return a more verbal response than ls
#Gives the information of each bash script in the current directory
#look for a specific script if pipped with grep
file ./*.sh

#fuser
#Identify processes using files or sockets
#List the process along with it's pid and owner
fuser -uv . 

#grep
#print lines that matches a pattern
#Look for a specific user from other commands
ps -aux | grep root

#host
#DNS lookup utility
#Look up the ip address of a site
host well.cs.ucr.edu

#ldd
#Print shared library dependencies
#Lok up the dependencies for the grep command
ldd /bin/grep

#lsof
#List open files
#Look for files opened by a specific user
lsof -u root

#mount
#Mount a filesystem
#Mount a partition to temperary /mnt/
#good for recovering data from a partition
mount -t ntfs /dev/sda1 mnt

#ps
#Report a snapshot of the current processes
#List all processes currently running by root
ps aux | grep root

#pkill
#Sends signal to processes based on process name given.
#
pkill -USR1 firefox

#netstat
#Print network infomations
#Look for listening TCP ports
netstat -lt

#renice
#alter priority of runnning processes
#

#rsync

#time

#ssh
#remote login into a server
#login into well.cs.ucr.edu
ssh -XY well.cs.ucr.edu

#stat

#strace

#uname

#wget

#didn't start this hw earlier :\
