#!/bin/bash

if [[ $1 == "h" ]] || [[ $1 == "" ]] || [[ $1 == "-h"]]
then
        echo "USAGE:"
        echo "To encrypt a file or folder without removing the source, parse its name"
        echo "i.e.:"
        echo "  encrypt.sh file/folder   "
        echo ""
        echo "To encrypt a file or folder removing the source, parse its name and add a 'r' parameter"
        echo "i.e.:"
        echo "  encrypt.sh file_folder r "
        exit
fi

tar cvfz /tmp/output.tar.gz $1

base64 /tmp/output.tar.gz > /tmp/output.64
rm /tmp/output.tar.gz
gpg -o $1.gpg --cipher-algo AES256 --symmetric /tmp/output.64
rm /tmp/output.64

if [[ $2 == "r" ]]
then
	rm -r $1
fi
