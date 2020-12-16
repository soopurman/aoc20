#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests
import itertools


def arrngmnts(adptrs):
    adptrs = [[i, 0] for i in adptrs]
    adptrs.append([adptrs[-1][0]+3, 0]) # for final adapter in the device
    adptrs.insert(0, [0,1]) # for charging outlet
    for i, j in enumerate(adptrs):
        for k in (1,2,3):
            try:
                n = adptrs[i+k]
            except IndexError:
                break
            if n[0] - j[0] <= 3:
                n[1] += j[1]
    return adptrs[-1][1]

    


def main(args):
    adptrs = sorted([int(num) for num in args.input.splitlines()])
    if args.arrangements:
        return arrngmnts(adptrs)
    prev = 0 # for the charging outlet
    ones = 0
    threes = 0
    for n in adptrs:
        diff = n - prev
        prev = n
        if diff == 1:
            ones += 1
        if diff == 3:
            threes += 1
    threes += 1 # for the final adapter in the device
    return ones * threes


if __name__ == '__main__':
    puzzle = re.findall(r'[^._]+', os.path.basename(__file__))

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', help='URL of puzzle input',
        default=f"https://adventofcode.com/2020/{puzzle[0]}/{puzzle[1]}/input")
    parser.add_argument('-arrangements', action='store_true', help='count valid arrangements of the numbers, rather than jumps between the numbers')
    args = parser.parse_args()

    jar = browsercookie.load()
    args.input = requests.get(args.input, cookies=jar).text

    print(main(args))
