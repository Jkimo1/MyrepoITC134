#!/bin/bash

echo -n "Print Message"

valid=0

while 
[ $valid == 0 ]

do
	read ans
	case $ans in
	yes|YES|y|Y ) echo Will print the message
		      echo The Message is cooler thanyou.
		      valid=1
		      ;;
	[nN][oO]    ) echo Will NOT print message
		      valid=1 ;;
	*	    ) echo Yes or No of some from please ;;
	esac
done
