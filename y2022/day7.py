from lib.utils import read_input

def go():

    input = read_input("input/2022:7.txt", split_lines=True)
    tree = {}
    paths = []

    for line in input:
        elements = line.split()
        if line.startswith('$ cd'):
            dir_name = elements[2]
            if dir_name == '..':
                paths.pop()
            else:
                path = f'{paths[-1]}_{dir_name}' if paths else dir_name
                paths.append(path)
                tree[path] = 0
        elif not (line.startswith('dir') or line.startswith('$ ls')):
            for path in paths:
                tree[path] += int(elements[0])
    
    # Part 1
    count = sum(n for n in tree.values() if n <= 100000)
    # Part 2
    REQUIRED_UPDATE_SPACE = 30_000_000 - (70_000_000 - tree['/'])
    dir_to_delete = 99_999_999
    for val in sorted(tree.values()):
        if val >= REQUIRED_UPDATE_SPACE:
            dir_to_delete = val
            break

    return count, dir_to_delete


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)