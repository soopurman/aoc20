#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests


def run(tape):
    ip = 0
    acc = 0
    visited = set()
    while ip < len(tape) and ip not in visited:
        visited.add(ip)
        acc += {'acc': tape[ip]['arg']}.get(tape[ip]['inst'], 0)
        ip += {'jmp': tape[ip]['arg']}.get(tape[ip]['inst'], 1)
    return ip, acc

def main(input, fix):
    tape = [dict(inst=i, arg=int(a)) for i, a in map(lambda l: l.split(), input.splitlines())]
    if not fix:
        return run(tape)[1]
    swap = {'jmp': 'nop', 'nop': 'jmp'}
    for cmd in tape:
        if cmd['inst'] in swap:
            cmd['inst'] = swap[cmd['inst']]
            ip, acc = run(tape)
            cmd['inst'] = swap[cmd['inst']]
            if ip == len(tape):
                return acc


if __name__ == '__main__':
    puzzle = re.findall(r'[^._]+', os.path.basename(__file__))

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', help='URL of puzzle input',
        default=f"https://adventofcode.com/2020/{puzzle[0]}/{puzzle[1]}/input")
    parser.add_argument('-fix', action='store_true', help='report accumulator after fixing courruption (instead of before second iteration of infinite loop)')
    args = parser.parse_args()

    jar = browsercookie.load()
    input = requests.get(args.input, cookies=jar).text

    print(main(input, args.fix))
