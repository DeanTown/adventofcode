from lib.utils import read_input
# https://realpython.com/python-eval-function/
def go():

    input = read_input("input/2022:7.txt", split_lines=True)
    file_structure = {}
    current_path = []

    for line in input:
        elements = line.split()
        if '$' in elements:
            if 'cd' in elements:
                dir_name = elements[2]
                if dir_name == '..':
                    val = file_structure[tuple(current_path)]
                    current_path.pop()
                    file_structure[tuple(current_path)] += val
                else:
                    current_path.append(dir_name)
                    file_structure[tuple(current_path)] = 0
        elif 'dir' not in elements:
            file_structure[tuple(current_path)] += int(elements[0])
    
    count = 0
    for val in file_structure.values():
        if val < 100_000:
            count += val

    return count, 2


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)