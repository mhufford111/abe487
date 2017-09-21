#!/bin/bash


if [[ $# -ne 2 ]]; then
     printf "Usage: hello-arg2.sh greeting name\n)"
     exit 1
     
fi

echo "${1}, ${2}!"

