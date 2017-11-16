#!/usr/bin/env python3

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(description='Argparse Python script')
    parser.add_argument('positional', metavar='file', help='BLAST tab output')
    parser.add_argument('-p', '--pct_id', help='Percent identity',
                        metavar='float', type=float, default=0)
    parser.add_argument('-e', '--evalue', help='',
                        metavar='float', type=float, default=None)
    return parser.parse_args()

# --------------------------------------------------
def main():
    args = get_args()
    pos_arg = args.positional
    int_arg = args.pct_id
    int_arg2 = args.evalue
    flds = 'qseqid sseqid pident useless1 useless2 useless3 useless4 useless5 useless6 useless7 evalue'.split()

    for line in open(pos_arg):
      row = dict(zip(flds, line.split('\t')))
      number = float(row['pident'])
      number2 = float(row['evalue'])
      if number >= int_arg and int_arg2 == None :
           print(row['qseqid'] + '\t' + row['sseqid'] +'\t' + row['pident'] + '\t' +  row['evalue'])
      if not int_arg2 == None and int_arg == 0:
           if number2 <= int_arg2 :
                print(row['qseqid'] + '\t' + row['sseqid'] +'\t' + row['pident'] + '\t' +  row['evalue'])
      if not int_arg == 0 and not int_arg2 == None:
           if number2 <= int_arg2 and number >= int_arg:
                print(row['qseqid'] + '\t' + row['sseqid'] +'\t' + row['pident'] + '\t' +  row['evalue'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
