#!/bin/bash


ip=`route -n | grep "UG" | awk '{print $2}'`
dev=`route -n | grep "UG" | awk '{print $8}'`
mask=`ifconfig $dev | grep -i mask | awk '{print $4}' | sed 's/Mask\:// '`
echo gateway: $ip netmask: $mask device: $dev
