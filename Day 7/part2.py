import re

with open('test_input.txt', 'r') as f:
    data = f.readlines()
bag_rules = []

for line in data:
    line = line.rstrip()
    line = line.split()
    bag_rules.append(line)

pertinent_rules = []

number_of_bags = 1
target_tint = 'shiny'
target_colour = 'gold'
answer = 0

def find_bags_inside(number_of_bags, target_tint, target_colour, bag_rules):
    for particular_rule in bag_rules:
        if particular_rule[0] == target_tint and particular_rule [1] == target_colour:
            pertinent_rule = particular_rule
    bags_contained = []
    for i in range(len(pertinent_rule)):
        try:
            number_of_bags = int(pertinent_rule[i])
            bags_contained.append(number_of_bags)
            bags_contained.append(pertinent_rule[i+1])
            bags_contained.append(pertinent_rule[i+2])

        except ValueError:
            pass
    return bags_contained

bags_contained = find_bags_inside(1, target_tint, target_colour, bag_rules)

for bag in bags_contained:
    number_of_bags = bag[0]
    target_tint = bag[1]
    target_colour = bag[2]
    new_bags = find_bags_inside(number_of_bags, target_tint, target_colour, bag_rules)
    bags_contained.append(new_bags)
