def is_sum_of(list_of_integers, integer):
    """

    :param list_of_integers: a list of integers to be summed
    :param integer: is this integer a sum of two of the numbers in the list of integers
    :return: True if it can; False if it can't
    """
    for number in list_of_integers:
        for other_number in list_of_integers:
            if number == other_number:
                pass
            else:
                test_number = number + other_number
                if test_number == integer:
                    return True
    return False

def open_the_code(filename, preamble_length):
    """
    :param filename: a file to be opened
    :param preamble_length: the length of the provided preamble
    :return: a tuple of the preamble and then the other numbers
    """
    with open(filename, 'r') as f:
        data = f.readlines()

    code_to_be_checked = []
    for line in data:
        line = int(line.rstrip())
        code_to_be_checked.append(line)

    preamble = code_to_be_checked[:preamble_length]
    code_to_be_checked = code_to_be_checked[preamble_length:]

    return preamble, code_to_be_checked


preamble, all_numbers = open_the_code('input.txt', 25)

for number_to_look_at in all_numbers:
    good_to_go = is_sum_of(preamble, number_to_look_at)
    if good_to_go == False:
        target_number = number_to_look_at
    preamble.append(number_to_look_at)
    preamble = preamble[1:]

print(target_number)

'''
---------------------------------------------------- PART 2 ----------------------------------------------------------
'''

preamble, all_numbers = open_the_code('input.txt', 25)
preamble_plus_all_numbers = preamble + all_numbers

def large_can_be_summed(list_of_integers, integer):
    """

    :param list_of_integers: a list of integers to be summed
    :param integer: is this integer a sum of a set of contiguous numbers in the list of integers
    :return: The set of contiguous numbers
    """

    for j in range(len(list_of_integers)):
        target_integer = integer
        contiguous_numbers = []
        for i in range(len(list_of_integers)):
            i = i+j
            if list_of_integers[i] == list_of_integers[j]:
                pass
            else:
                target_integer -= list_of_integers[i]
                contiguous_numbers.append(list_of_integers[i])
                if target_integer == 0:
                    return contiguous_numbers
                elif target_integer < 0:
                    break
    return contiguous_numbers

target_list = large_can_be_summed(preamble_plus_all_numbers, target_number)

target_list.sort()

answer = target_list[0] + target_list[-1]

print(answer)

