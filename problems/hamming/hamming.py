#!/usr/bin/env python3
import os
import sys

args = sys.argv[1:]

if len(args) != 2:
    print('usage')
    sys.exit(1)

x = args[0]
y = args[1]

count = abs(len(x) - len(y))

for i in range(min(len(x), len(y))):
    if x[i] != y[i]:
        count += 1

print(count)
