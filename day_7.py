#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests


def up(input, targets, holders=None):
    if not holders:
        holders = set()
    new_holders = set()
    for line in input.splitlines():
        container, contents = line.split('contain')
        for t in targets:
            if t in contents:
                bag = container.split(' bag')[0]
                if bag not in holders:
                    new_holders.add(bag)
    if new_holders:
        holders.update(new_holders)
        holders.update(up(input, new_holders, holders))
    return holders


def down(input, target):
    result = 0
    for line in input.splitlines():
        if line.startswith(target):
            for bags in line.split('contai')[1].split('bag'):
                bags = bags.split()
                if len(bags) > 1:
                    mult = bags[1]
                    bag = ' '.join(bags[2:])
                    if mult != 'no':
                        result += int(mult) * (1 + down(input, bag))
    return result


if __name__ == '__main__':
    puzzle = re.findall(r'[^._]+', os.path.basename(__file__))

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', help='URL of puzzle input',
        default=f"https://adventofcode.com/2020/{puzzle[0]}/{puzzle[1]}/input")
    parser.add_argument('-target', default='shiny gold', help='type of bag we want to find storage for')
    parser.add_argument('-down', action='store_true', help='count down the contents of the target (as opposed to up its containers)')
    args = parser.parse_args()

    jar = browsercookie.load()
    input = requests.get(args.input, cookies=jar).text

    if not args.down:
        print(len(up(input, {args.target})))
    else:
        print(down(input, args.target))
