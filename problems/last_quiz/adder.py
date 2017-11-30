#!/usr/bin/env python3
import os
import sys

args = sys.argv[1:]

if len(args) != 2:
    print('usage')
    sys.exit(1)

x = args[0]
y = args[1]

if x.isdigit() and y.isdigit():
    z = int(x) + int(y)
    print(z)
elif not x.isdigit() and not y.isdigit():
    print(x + ' and ' + y)

else:
    print('Cannot combine number and string')
    exit(1)

