import re

with open('input.txt', 'r') as f:
    data = f.readlines()
bag_rules = []

for line in data:
    line = line.rstrip()
    line = line.split()
    bag_rules.append(line)

pertinent_rules = []

target_tint = 'shiny'
target_colour = 'gold'

for rule in bag_rules:
    if rule[0] == target_tint and rule[1] == target_colour or rule[-3] == 'no':
        bag_rules.remove(rule)

bag_rules_copy = bag_rules.copy()


def find_container_bags(target_tint, target_colour, bag_rules):
    outer_nest_rules = []
    for particular_rule in bag_rules:
        for j in range(len(particular_rule)):
            if particular_rule[j] == target_tint:
                if particular_rule[j + 1] == target_colour:
                    outer_nest_rules.append(particular_rule)
    if outer_nest_rules == []:
        return []
    else:
        return outer_nest_rules


pertinent_rules = (find_container_bags(target_tint, target_colour, bag_rules))
for rule in pertinent_rules:
    bag_rules.remove(rule)
count = 0
temp_rules = None

loop_ended = False

while not loop_ended:
    for bag in pertinent_rules:
        target_colour = bag[1]
        target_tint = bag[0]
        temp_rules = find_container_bags(target_tint, target_colour, bag_rules)
        for rule in temp_rules:
            if rule not in pertinent_rules:
                pertinent_rules.append(rule)
                bag_rules.remove(rule)
    loop_ended = True

print(len(pertinent_rules))