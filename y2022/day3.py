import string as s
from lib.utils import read_input

def go():

    input = read_input("input/2022:3.txt", split_lines=True)

    # PART 1

    split = [[line[:len(line)//2], line[len(line)//2:]] for line in input]
    duplicates = find_duplicates(split)
    part1 = calculate_priority(duplicates)

    # PART 2

    split = [input[i:i+3] for i in range(0, len(input), 3)]
    duplicates = find_duplicates(split)
    part2 = calculate_priority(duplicates)

    return part1, part2

def find_duplicates(split):
    duplicates = []
    for first, *rest in split:
        while True:
            char = first[0]
            if all(char in string for string in rest):
                duplicates.append(char)
                break
            else:
                first = list(filter(lambda x: x != char, first))
    return duplicates

def calculate_priority(chars):
    priority_map = {c: i+1 for i, c in enumerate(list(s.ascii_lowercase) + list(s.ascii_uppercase))}
    priority = 0
    for char in chars:
        priority += priority_map[char]
    return priority


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)