#!/usr/bin/env python3
#!/usr/bin/env python3
# Kmer counter

from collections import Counter
import sys, string
import os
import os.path
from pathlib import Path

args = sys.argv[1:]
if len(args) < 1:
        print("Usage: kmer_counter.py SEQ")
        sys.exit(1)

kmer_size = 3

input = args[0].upper()
nkmers = len(input) % 3

if kmer_size > len(input):
        print('There are no {}-mers in "{}"'.format(kmer_size, args[1]))
        sys.exit(1)

kmer = {}

s = ""
i = 0
add = ""
j = 0
k = 0

while i < len(input) - 2:
	add = ""
	j = i
	k = i 
	while j < 3 + i:
		add += input[j]
		if add == "UUU" or add == "UUC":
			s += "F"
		if add == "UUA" or add == "UUG" or add == "CUU" or add == "CUC" or add == "CUA" or add == "CUG":
			s += "L"
		if add == "AUU" or add == "AUC" or add == "AUA":
			s += "I"
		if add == "AUG":
			s += "M"
		if add == "GUU" or add == "GUC" or add == "GUA" or add == "GUG":
			s += "V"
		if add == "UCU" or add == "UCC" or add == "UCA" or add == "UCG":
			s += "S"
		if add == "CCU" or add == "CCC" or add == "CCA" or add == "CCG":
			s += "P"
		if add == "ACU" or add == "ACC" or add == "ACA" or add == "ACA" or add == "ACG":
			s += "T"
		if add == "GCU" or add == "GCC" or add == "GCA" or add == "GCG":
			s += "A"
		if add == "UAU" or add == "UAC":
			s += "Y"
		if add == "UAA" or add == "UAG" or add == "UGA":
			break
		if add == "CAU" or add == "CAC":
			s += "H"
		if add == "CAA" or add == "CAG":
			s += "Q"
		if add == "AAU" or add == "AAC":
			s += "N"
		if add == "AAA" or add == "AAG":
			s += "K"
		if add == "GAU" or add == "GAC":
			s += "D"
		if add == "GAA" or add == "GAG":
			s += "E"
		if add == "UGU" or add == "UGC":
			s += "C"
		if add == "UGG":
			s += "W"
		if add == "CGU" or add == "CGC" or add == "CGA" or add == "CGG" or add == "AGA" or add == "AGG":
			s += "R"
		if add == "AGU" or add == "AGC":
			s += "S"
		if add == "GGU" or add == "GGC" or add == "GGA" or add == "GGG":
			s += "G"
		j += 1
	add = ""
	i += 3

print('{}'.format(s))
