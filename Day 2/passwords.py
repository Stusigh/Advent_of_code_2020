with open('input.txt', 'r') as f:
    data = f.readlines()
rules_and_passwords = []
for line in data:
    line = line.rstrip()
    rule_and_password = line.split(":")
    rules_and_passwords.append(rule_and_password)

number_of_valid_passwords = 0
number_of_invalid_passwords = 0

for rule_and_password in rules_and_passwords:

    '''
    Let's just do it with one first. Get all the elements out. 
    password_to_check
    character_to_check
    max_number_of_characters
    min_number_of_characters
    '''

    password_to_check = rule_and_password.pop()[1:]

    character_to_check = rule_and_password[0][-1]

    rule_to_check = rule_and_password[0][:-2]
    max_number_of_characters = int(rule_to_check.split('-')[1])
    min_number_of_characters = int(rule_to_check.split('-')[0])

    character_count_in_password = 0

    for character in password_to_check:
        if character == character_to_check:
            character_count_in_password += 1
    if min_number_of_characters <= character_count_in_password <= max_number_of_characters:
        print('Valid Password')
        number_of_valid_passwords += 1
    else:
        print('Invalid Password')
        number_of_invalid_passwords += 1

print(number_of_valid_passwords)