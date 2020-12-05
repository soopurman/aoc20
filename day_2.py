#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests

puzzle = re.findall(r'[^._]+', os.path.basename(__file__))

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-input', help='URL of puzzle input',
    default=f"https://adventofcode.com/2020/{puzzle[0]}/{puzzle[1]}/input")
parser.add_argument('-official', action='store_true',
    help='apply "official" (as opposed to "old") interpretation of password database entries')
args = parser.parse_args()

jar = browsercookie.load()

input = requests.get(args.input, cookies=jar)

database = [re.search(r'^(\d+)-(\d+) ([^:]+): (.*)$', entry) for entry in input.iter_lines(decode_unicode=True)]

result = 0

for entry in database:
    fields = [int(entry.group(i)) if i < 3 else entry.group(i) for i in range(1,5)]
    if args.official:
        result += 1 if f"{fields[3][fields[0]-1]}{fields[3][fields[1]-1]}".count(fields[2]) == 1 else 0
    else:
        result += 1 if fields[0] <= fields[3].count(fields[2]) <= fields[1] else 0

print(result)
