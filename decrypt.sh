#!/bin/bash

if [[ $1 == "h" ]] || [[ $1 == "" ]] || [[ $1 == "-h"]]
then
	echo "USAGE:"
	echo "To decrypt a GPG file without removing the source, parse its filename (WITHOUT EXTENSION)"
	echo "i.e.:"
	echo "	decrypt.sh file_noext	"
	echo ""
	echo "To decrypt a GPG file removing the source, parse its filename (WITHOUT EXTENSION) and add a 'r' parameter"
	echo "i.e.:"
	echo "	decrypt.sh file_noext r	"
	exit
fi

gpg -o /tmp/output.64 --decrypt $1.gpg 
if [[ $2 == "r" ]]
then
	rm $1.gpg
fi

base64 -d /tmp/output.64 > /tmp/output.tar.gz
rm /tmp/output.64
tar xvfz /tmp/output.tar.gz
rm /tmp/output.tar.gz
