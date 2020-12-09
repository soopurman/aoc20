#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests


def main(input, find_empty):
    collected_boarding_pass_seat_ids = [int(re.sub(r'[FfLl]', '0', re.sub(r'[bBrR]', '1', i.strip())), base=2) for i in input.iter_lines(decode_unicode=True)]
    collected_boarding_pass_seat_ids.sort()
    if not find_empty:
        return collected_boarding_pass_seat_ids[-1]
    prev = collected_boarding_pass_seat_ids[0]
    for i in collected_boarding_pass_seat_ids[1:]:
        if i - prev > 1:
            return i - 1
        prev = i


if __name__ == '__main__':
    puzzle = re.findall(r'[^._]+', os.path.basename(__file__))

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', help='URL of puzzle input',
        default=f"https://adventofcode.com/2020/{puzzle[0]}/{puzzle[1]}/input")
    parser.add_argument('-find_empty', action='store_true', help='find empy seat (as opposed to find highest seat id)')
    args = parser.parse_args()

    jar = browsercookie.load()
    input = requests.get(args.input, cookies=jar)

    print(main(input, args.find_empty))
