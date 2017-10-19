#!/usr/bin/env python3

from collections import Counter
from collections import defaultdict
import sys, string
import os
import os.path

args = sys.argv[1:]
if len(args) < 2:
        print("Usage: kmer_counter.py LEN STR")
        sys.exit(1)

if args[0].isdigit():
        kmer_size = int(args[0])
else:
        print('Kmer size "{}" is not a number'.format(args[0]))
        sys.exit(1)

if(kmer_size<=0):
        print('Kmer size "{}" must be > 0'.format(kmer_size))

input = args[1]

nkmers = len(input) - kmer_size + 1

if kmer_size > len(input):
	print('There are no () mers in "{}"'.format(kmer_size, args[1]))

kmers = {}

i = 0
add = ""
j = 0
z = 0

while i < nkmers:
	add = ""
	j = 0
	z = i
	while j < kmer_size:
		add += input[z+j]
		j += 1
	if add in kmers:
		kmers[add] += 1
	else:
		kmers[add] = 1
	i += 1

print('{}'.format(input))

for x in sorted(kmers):
	print x, kmers[x]
