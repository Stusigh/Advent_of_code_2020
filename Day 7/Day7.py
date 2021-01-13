with open('test_input.txt', 'r') as f:
    data = f.readlines()
bag_rules = []
for line in data:
    line = line.rstrip()
    line = line.split()
    bag_rules.append(line)
for line in bag_rules:
    if line[0:2] == ['shiny', 'gold']:
        primary_line = line


def find_bags_inside(target_tint, target_colour, bag_rules, count=0):
    for rule in bag_rules:
        if rule[0] == target_tint and rule[1] == target_colour:
            rule_to_look_at = rule
            break
    if rule_to_look_at[-3:] == ['no', 'other', 'bags.']:
        return count
    else:
        number_of_different_bags_inside = (len(rule_to_look_at) // 4) - 1
        rule_to_look_at = rule_to_look_at[4:]
        for i in range(number_of_different_bags_inside):
            count += int(rule_to_look_at[i * 4])
            target_tint = rule_to_look_at[(i * 4) + 1]
            target_colour = rule_to_look_at[(i * 4) + 2]
            print(count)
            result = find_bags_inside(target_tint, target_colour, bag_rules, count)
            return result


a = find_bags_inside('shiny', 'gold', bag_rules)
