#!/usr/bin/env python3

#!/usr/bin/env python3
from collections import Counter
import sys, string
import os

args = sys.argv

if len(args) < 2:
        script = os.path.basename(args[0])
        print('Usage: gc.py STRING'.format(script))
        sys.exit(1)

word = args[1]
numVowels = 0
numVowels2 = 0
vowels1 = 'GCgc'
vowels2 = 'ATat'

for char in word:
	if char in vowels1:
		numVowels += 1
	else:
		numVowels2 += 1

percent = int(numVowels / (numVowels2 + numVowels) * 100)

print("%i%% GC" % (percent))  

