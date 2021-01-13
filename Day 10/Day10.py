# -*- coding: utf-8 -*-
"""
Date: 12/17/2020
Author: Stuart Page
"""
with open('input.txt', 'r') as f:
    data = f.readlines()
list_of_joltages = []
for line in data:
    line = int(line.rstrip())
    list_of_joltages.append(line)

built_in_adaptor_rating = max(list_of_joltages) + 3
list_of_joltages.sort()

joltage_differences = []
for i in range(len(list_of_joltages)):
    if i == 0:
        joltage_differences.append(abs(0-list_of_joltages[0]))
    else:
        joltage_differences.append(list_of_joltages[i]-list_of_joltages[i-1])

joltage_differences.append(built_in_adaptor_rating - list_of_joltages[-1])

three_count = 0
one_count = 0


for joltage in joltage_differences:
    if joltage == 1:
        one_count += 1
    elif joltage == 3:
        three_count += 1

answer = one_count * three_count
print(one_count)
print(three_count)
print(answer)
