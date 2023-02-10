from lib.utils import read_input
# https://realpython.com/python-eval-function/
def go():

    input = read_input("input/2022:7.txt", split_lines=True)
    file_structure = {}
    current_path = []

    for line in input:
        elements = line.split()
        # The line is a command
        if '$' in elements:
            if 'cd' in elements:
                dir_name = elements[2]
                if dir_name == '..':
                    current_path.pop()
                else:
                    # Need to check if a dict already exists for this path, if not then create one
                    current_path.append(dir_name)
                    if dir_name == '/':
                        # This is the root directory -- don't create a key for it
                        continue
                    key = tuple(current_path)
                    print(key)
                    file_structure[key] = {}
                    print(file_structure)
                    print(current_path)
            elif 'ls' in elements:
                pass
        # The line is a file/director representation
        else:
            pass
    return 1, 2


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)