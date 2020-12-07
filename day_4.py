#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests


def valid(record, check):
    min_flds_in_valid_rec = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    if check:
        pass
    else:
        return all(fld in record for fld in min_flds_in_valid_rec)


def main(input, check):
    candidates = [{fld[0]: fld[1] for fld in map(lambda s: s.split(':'), rec.split())} for rec in re.split(r'^\s*$', input.text, flags=re.MULTILINE)]
    passports = [rec for rec in candidates if valid(rec, check)]
    return len(passports)


if __name__ == '__main__':
    puzzle = re.findall(r'[^._]+', os.path.basename(__file__))

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-input', help='URL of puzzle input',
        default=f"https://adventofcode.com/2020/{puzzle[0]}/{puzzle[1]}/input")
    parser.add_argument('-check', action='store_true', help='check for valid values in every field of each record')
    args = parser.parse_args()

    jar = browsercookie.load()
    input = requests.get(args.input, cookies=jar)

    print(main(input, args.check))
