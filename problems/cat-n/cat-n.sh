#!/bin/bash

number=1;

if [[ $# == 0 ]]; then
	echo "Usage: cat-n.sh file\n)"
        exit 1

fi

if [[ -f ${1:-'srr.txt'} ]]; then

FILE=$1
number=1

	while read -r LINE; do
		echo "$number $LINE"
		let "number++"
	done < "$FILE"
else
	printf "\"${1:-'srr.txt'}\" is not a file\n)"
	exit 1
fi

