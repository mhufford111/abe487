#!/usr/bin/env python3
import os
import sys
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

k = 3
Ros = [line.strip() for line in open(sys.argv[1])]
i = 2
while i < len(Ros):
    if not Ros[i].startswith('>') and not Ros[i-1].startswith('>'):
        Ros[i-1] += Ros[i]
        del Ros[i]
        i -= 1
    i += 1
dna = {}
for i in range(0,len(Ros),2):
    dna[Ros[i][1:]] = Ros[i+1]
for first in dna.keys():
    for second in dna.keys():
        if first != second and dna[first][len(dna[first])-k:] == dna[second][0:k]:
            print(first + " " + second)

sys.exit(0)
