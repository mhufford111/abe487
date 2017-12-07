#!/usr/bin/env python3
import re
from collections import Counter
import sys, string
import os
import os.path
from pathlib import Path

args = sys.argv[1:]
if len(args) < 1:
	print('usage')
	sys.exit(1)

if not Path(sys.argv[1]).exists():
	print('usage')
	sys.exit(1)

x = [line.rstrip('\n') for line in open(sys.argv[1])]
y = [line.rstrip('\n') for line in open(sys.argv[2])]
z = 0
q = 0
i = 0
finalval = 0

while z < 3 :
    s = x[z]
    #print(s)
    while q < 3 :
        t = y[q]
        #print(t)
        for i in range(len(s)-len(t)+1):
            if s[i:i+len(t)] == t:
                finalval = finalval + 1
        q = q + 1
    q = 0
    z = z + 1

print(finalval)

sys.exit(0)
