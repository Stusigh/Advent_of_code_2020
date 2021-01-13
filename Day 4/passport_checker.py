# -*- coding: utf-8 -*-
"""
Date: 12/4/2020
Author: Stuart Page
"""
import re

passport_data = []
passports_to_check = [[]]
passport_counter = 0
with open('input.txt', 'r') as f:
    data = f.readlines()
for line in data:
    line = line.rstrip()
    passport_data.append(line)
for line in passport_data:
    if line == '':
        passports_to_check.append([])
        passport_counter += 1
    else:
        passports_to_check[passport_counter].append(line)
other_passports = []
for passport in passports_to_check:
    empty_string = ""
    for element in passport:
        empty_string += element
    other_passports.append(empty_string)
passports_to_check = other_passports

regex_check_ecl = re.compile(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)')
regex_check_pid = re.compile(r'pid:\d\d\d\d\d\d\d\d\d')
regex_check_eyr = re.compile(r'eyr:(\d{4})')
regex_check_hcl = re.compile(r'hcl:#(\d|[a-f]\d|[a-f]\d|[a-f]\d|[a-f]\d|[a-f]\d|[a-f]\d|[a-f]\d|[a-f]\d|[a-f])')
regex_check_byr = re.compile(r'byr:(\d\d\d\d)')
regex_check_iyr = re.compile(r'iyr:(\d\d\d\d)')
regex_check_cid = re.compile(r'cid')
regex_check_hgt = re.compile(r'hgt:((\d\d)in|(\d\d\d)cm)')

invalid = 0
valid = 0

for passport in passports_to_check:
    ecl = regex_check_ecl.search(passport)
    pid = regex_check_pid.search(passport)
    eyr = regex_check_eyr.search(passport)
    hcl = regex_check_hcl.search(passport)
    byr = regex_check_byr.search(passport)
    iyr = regex_check_iyr.search(passport)
    # cid = regex_check_cid.search(passport)
    hgt = regex_check_hgt.search(passport)
    if ecl == None:
        invalid += 1
    elif pid == None:
        invalid += 1
    elif eyr == None:
        invalid += 1
    elif hcl == None:
        invalid += 1
    elif byr == None:
        invalid += 1
    elif iyr == None:
        invalid += 1
    # elif cid == None:
    #     invalid += 1
    elif hgt == None:
        invalid += 1
    elif not 2020 <= int(eyr.group(1)) <= 2030:
        invalid += 1
    elif not 1920 <= int(byr.group(1)) <= 2002:
        invalid += 1
    elif not 2010 <= int(iyr.group(1)) <= 2020:
        invalid += 1
    elif hgt.group(2) == None:  # cm rules
        if not 150 <= int(hgt.group(3)) <= 193:
            invalid += 1
        else:
            valid += 1
    elif hgt.group(3) == None:  # inches rules
        if not 59 <= int(hgt.group(2)) <= 76:
            invalid += 1
        else:
            valid += 1
    else:
        valid += 1

print('done')
print(str(valid) + ' valid passports.')
print(str(invalid) + ' invalid passports.')
