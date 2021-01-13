import string

with open('input.txt', 'r') as f:
    data = f.readlines()
answer_data = []
group_count = 0
grouped_answers = [[]]

for line in data:
    line = line.rstrip()
    answer_data.append(line)

for line in answer_data:
    if line == '':
        grouped_answers.append([])
        group_count += 1
    else:
        grouped_answers[group_count].append(line)

def characters_in_common(a_list):
    '''

    :param string: takes in a list containing one or more strings of characters
    :return: a string of all the characters all the strings have in common
    '''
    if len(a_list) == 1:
        match = []
        for item in a_list:
            for character in item:
                match.append(character)
        return match

    comparator = list(a_list[0])
    potential_matches = comparator.copy()
    for character in comparator:
        for word in a_list[1:]:
            if character not in word:
                if character in potential_matches:
                    potential_matches.remove(character)
    return potential_matches



total_answers = 0
for answer in grouped_answers:
    answer_in_common = characters_in_common(answer)
    all_questions = list(string.ascii_lowercase)
    for individual_answer in answer_in_common:
         if individual_answer in all_questions:
             all_questions.remove(individual_answer)
    number_of_answers = 26 - len(all_questions)
    total_answers += number_of_answers

print(total_answers)












# peaches = []
#
# for group_answer in grouped_answers:
#     blank_string = ''
#     for answer in group_answer:
#         blank_string += answer
#     peaches.append(blank_string)
#
# grouped_answers = peaches
#
#
# sum_of_answer_totals = 0
# for group_answer in grouped_answers:
#     all_questions = list(string.ascii_lowercase)
#     for individual_answer in group_answer:
#         if individual_answer in all_questions:
#             all_questions.remove(individual_answer)
#     number_of_answers = 26 - len(all_questions)
#     sum_of_answer_totals += number_of_answers