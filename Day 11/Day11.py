# -*- coding: utf-8 -*-
"""
Date: 12/17/2020
Author: Stuart Page
"""
with open('test_input.txt', 'r') as f:
    data = f.readlines()
seats = []
for line in data:
    line = line.rstrip()
    line=line.split()
    seats.append(line)

seats_copy = seats.copy()

