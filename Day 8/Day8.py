with open('input.txt', 'r') as f:
    data = f.readlines()
program_code = []
for line in data:
    line = line.rstrip()
    line = line.split()
    program_code.append(line)


# use the index() method
def try_out_code(part_of_program_code):
    accumulator = 0
    lines_executed = []
    done = False
    line_executing = 0
    while done == False:
        try:
            if 'acc' in program_code[line_executing][0]:
                if line_executing in lines_executed:
                    return False
                lines_executed.append(line_executing)
                accumulator += int(program_code[line_executing][1])
                line_executing += 1
            if 'jmp' in program_code[line_executing][0]:
                if line_executing in lines_executed:
                    return False
                lines_executed.append(line_executing)
                line_executing += int(program_code[line_executing][1])
            if 'nop' in program_code[line_executing][0]:
                if line_executing in lines_executed:
                    return False
                lines_executed.append(line_executing)
                line_executing += 1
        except IndexError:
            return accumulator
    return accumulator

def change_back(program_code, line_changed):
    if program_code[line_changed][0] == 'jmp':
        program_code[line_changed][0] = 'nop'
    elif program_code[line_changed][0] == 'nop':
        program_code[line_changed][0] = 'jmp'

def code_modifier(program_code, lines_tried):
    line_changed = False
    if try_out_code(program_code) == False:
        while line_changed == False:
            for i in range(len(program_code)):
                if i not in lines_tried:
                    if program_code[i][0] == 'nop':
                        program_code[i][0] = 'jmp'
                        lines_tried.append(i)
                        line_changed = True
                        break
                    elif program_code[i][0] == 'jmp':
                        program_code[i][0] = 'nop'
                        lines_tried.append(i)
                        line_changed = True
                        break
    return program_code, lines_tried, i

def lets_find_the_answer(program_code):
    answer = False
    lines_tried = []
    while answer == False:
        if try_out_code(program_code) == False:

            tuple_of_program_code_and_lines_tried_and_line_changed = code_modifier(program_code, lines_tried)
            lines_tried = tuple_of_program_code_and_lines_tried_and_line_changed[1]
            answer = try_out_code(tuple_of_program_code_and_lines_tried_and_line_changed[0])
            change_back(program_code, tuple_of_program_code_and_lines_tried_and_line_changed[2])
    return answer


print(lets_find_the_answer(program_code))