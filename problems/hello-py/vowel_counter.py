#!/usr/bin/env python3
from collections import Counter
import sys, string
import os

args = sys.argv

if len(args) < 2:
        script = os.path.basename(args[0])
        print('Usage: vowel_counter.py STRING'.format(script))
        sys.exit(1)

word = args[1]
numVowels = 0
#vowels = list('a,e,i,o,u')
vowels = 'aeiou'

for char in word:
        if char in vowels:
                numVowels += 1

verb = 'is ' if numVowels == 1 else 'are '
noun = 'vowel ' if numVowels == 1 else 'vowels '
print('There ' + verb + str(numVowels) + ' ' +  noun + 'in "' + word + '."')
