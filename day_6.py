#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests
import string


def main(input, intersect):
    if intersect:
        agg = set(string.ascii_lowercase).intersection
    else:
        agg = set().union
    return sum([len(agg(*[set(l) for l in rec.splitlines()])) for rec in input.text.split('\n\n')])


if __name__ == '__main__':
    puzzle = re.findall(r'[^._]+', os.path.basename(__file__))

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', help='URL of puzzle input',
        default=f"https://adventofcode.com/2020/{puzzle[0]}/{puzzle[1]}/input")
    parser.add_argument('-all', action='store_true', help='count questions to which all (instead of "any") group members answered "yes"')
    args = parser.parse_args()

    jar = browsercookie.load()
    input = requests.get(args.input, cookies=jar)

    print(main(input, args.all))
