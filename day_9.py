#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests
import itertools


def main(args):
    ciphertext = [int(num) for num in args.input.splitlines()]
    for i in range(args.preamble, len(ciphertext)):
        if not any(sum(c) == ciphertext[i] for c in itertools.combinations(ciphertext[i - args.preamble:i], 2)):
            if not args.weak:
                return ciphertext[i]
            else:
                for j in range(0, len(ciphertext) - 3):
                    for k in range(3, len(ciphertext)):
                        if sum(ciphertext[j:k]) == ciphertext[i]:
                            return max(ciphertext[j:k]) + min(ciphertext[j:k])
                        if sum(ciphertext[j:k]) > ciphertext[i]:
                            break


if __name__ == '__main__':
    puzzle = re.findall(r'[^._]+', os.path.basename(__file__))

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', help='URL of puzzle input',
        default=f"https://adventofcode.com/2020/{puzzle[0]}/{puzzle[1]}/input")
    parser.add_argument('-preamble', type=int, default=25, help='length of preamble in ciphertext')
    parser.add_argument('-weak', action='store_true', help='report so-called "encryption weakness" (as opposed to first invalid datum)')
    args = parser.parse_args()

    jar = browsercookie.load()
    args.input = requests.get(args.input, cookies=jar).text

    print(main(args))
