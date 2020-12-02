#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests
import itertools
import functools
import operator

puzzle = re.findall(r'[^._]+', os.path.basename(__file__))

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-input', help='URL of puzzle input',
    default=f"https://adventofcode.com/2020/{puzzle[0]}/{puzzle[1]}/input")
parser.add_argument('-entries', type=int, help='number of entries to combine', default=2)
parser.add_argument('-sum', type=int, help='additive value to find', default=2020)
args = parser.parse_args()

jar = browsercookie.load()

input = requests.get(args.input, cookies=jar)

for c in itertools.combinations([int(i) for i in input.iter_lines()], args.entries):
    if sum(c) == args.sum:
        print(functools.reduce(operator.mul,c))
