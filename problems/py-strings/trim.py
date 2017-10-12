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

input = args[0]
cut = 5

if len(args) == 2:
	cut = int(args[1])

if Path(sys.argv[1]).exists():
	if os.path.isfile(input):
		for line in open(input):
			print(line[:cut])
else:
	print(input[:cut])
