#!/usr/bin/env python3
"""say hello to the arguments"""

import sys
import os
     
def main():
	args = sys.argv
	
	if len(args) < 2:
		script = os.path.basename(args[0])
		print('Usage: {} NAME [NAME2 ...]'.format(script))
		sys.exit(1)
	
	sys.stdout.write
	counter=0
	counter2=0

	for name in args[1:]:
		counter += 1
	sys.stdout.write("Hello to the {}".format(counter) + ' of you:')
	
	if len(args) == 3:
		for name in args[1:]:
			sys.stdout.write(' ' + name)
			if counter2 == 0:
				sys.stdout.write(' and')
				counter2 += 1
		sys.stdout.write('!\n')
	if counter > 1:
		if len(args) != 3:
			for name in args[1:]:
				counter2 += 1
				if counter2 < counter:
					sys.stdout.write(' ' + name + ',')
		
			if counter2 == counter:
				sys.stdout.write(' and ' + name + '!\n')    

	if counter == 1:
		sys.stdout.write(' ' + name + '!\n')

if __name__ == '__main__':
	main()
