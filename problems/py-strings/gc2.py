#!/usr/bin/env python3

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
	script = os.path.basename(sys.argv[1])
	print("\"%s\" is not a file" % (sys.argv[1]))
	sys.exit(1)

file = open(sys.argv[1], "r")

count = 0
i = 0
linetotal = 0

while True:
	count = 0
	line = file.readline()
	if not line: break
	i = 0
	while i < len( line ):
		char = line[i]
		if not char: break
		if char == 'G' or char == 'g' or char == 'C' or char == 'c':
			count += 1
		i += 1
		linetotal += 1
	print("%i" % (int((count/(linetotal-1))*100)))
	linetotal = 0


