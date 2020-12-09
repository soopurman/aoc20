#!/usr/bin/env python3
'''Advent of Code 2020'''

import re
import os
import argparse
import browsercookie
import requests


def valid(rec, check):
    min_flds_in_valid_rec = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    if not all(fld in rec for fld in min_flds_in_valid_rec):
        return False
    if not check:
        return True
    if not re.fullmatch(r'\d{9}', rec['pid']):
        return False
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', rec['hcl']):
        return False
    if not re.fullmatch(r'(amb|blu|brn|gry|grn|hzl|oth)', rec['ecl']):
        return False
    if not re.fullmatch(r'1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in', rec['hgt']):
        return False
    if not (re.fullmatch(r'\d{4}', rec['byr']) and 1920 <= int(rec['byr']) <= 2002):
        return False
    if not (re.fullmatch(r'\d{4}', rec['iyr']) and 2010 <= int(rec['iyr']) <= 2020):
        return False
    if not (re.fullmatch(r'\d{4}', rec['eyr']) and 2020 <= int(rec['eyr']) <= 2030):
        return False
    return True


def main(input, check):
    candidates = [dict(fld.split(':') for fld in rec.split()) for rec in re.split(r'^\s*$', input.text, flags=re.MULTILINE)]
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
