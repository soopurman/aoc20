#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests


def run(input):
    tape = [dict(inst=i, arg=int(a)) for i, a in map(lambda l: l.split(), input.splitlines())]
    ip = 0
    acc = 0
    while tape[ip].setdefault('visits', 0) < 1:
        tape[ip]['visits'] += 1
        acc += {'acc': tape[ip]['arg']}.get(tape[ip]['inst'], 0)
        ip += {'jmp': tape[ip]['arg']}.get(tape[ip]['inst'], 1)
    return acc


if __name__ == '__main__':
    puzzle = re.findall(r'[^._]+', os.path.basename(__file__))

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', help='URL of puzzle input',
        default=f"https://adventofcode.com/2020/{puzzle[0]}/{puzzle[1]}/input")
    args = parser.parse_args()

    jar = browsercookie.load()
    input = requests.get(args.input, cookies=jar).text

    print(run(input))
