from lib.utils import read_input
from copy import deepcopy

def go():

    input = read_input("input/2022:5.txt", split_lines=True)
    start_stacks = build_starting_stacks(input)

    # PART 1

    stacks = execute_moves(input, deepcopy(start_stacks), reverse=True)
    part1 = assemble_output(stacks)

    # PART 2

    stacks = execute_moves(input, deepcopy(start_stacks))
    part2 = assemble_output(stacks)

    return part1, part2

def build_starting_stacks(input):
    stacks = []
    stack_lines = []
    while True:
        line = input.pop(0)
        split = [line[i:i+4].strip(' []') for i in range(0, len(line), 4)]
        # If we get to the bottom of the stack descriptions, then break the loop
        if all(string.isnumeric() for string in split):
            stacks = [[] for _ in range(len(split))]
            input.pop(0) # Remove blank line
            break
        stack_lines.append(split)
    # Build the stacks from the stack lines using the total number of stacks
    for line in stack_lines:
        for index, value in enumerate(line):
            if value != '':
                stacks[index].insert(0, value)    
    return stacks

def execute_moves(input, stacks, reverse=False):
    for line in input:
        qty, target, dest = [int(num)-1 for num in line.split()[1::2]]
        qty += 1
        stacks[target], moved = stacks[target][:-qty], stacks[target][-qty:]
        if reverse: moved.reverse()
        stacks[dest].extend(moved)
    return stacks

def assemble_output(stacks):
    output = ''
    for stack in stacks:
        output += stack[-1]
    return output


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)