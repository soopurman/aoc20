#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests


def trees_in_slope(map,down,over):
    result = vert = horiz = 0

    while vert < len(map):
        result += 1 if map[vert][horiz % len(map[vert])] == '#' else 0
        vert += down
        horiz += over

    return(result)


def main(input, slopes):
    map = input.splitlines()
    result = 1

    for slope in slopes.split(','):
        result *= trees_in_slope(map,*[int(i) for i in slope.split('/')]) if slope else 1

    return(result)


if __name__ == '__main__':
    puzzle = re.findall(r'[^._]+', os.path.basename(__file__))

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', help='URL of puzzle input',
        default=f"https://adventofcode.com/2020/{puzzle[0]}/{puzzle[1]}/input")
    parser.add_argument('slopes', nargs='?', default='1/3',
        help='comma separated list of toboggan slopes to check for trees, in "down/over" notation')
    args = parser.parse_args()

    jar = browsercookie.load()
    input = requests.get(args.input, cookies=jar).text

    print(main(input, args.slopes))
