from lib.utils import read_input

def go():

    input = read_input("input/2022:6.txt")

    part1 = search_marker(input, 4)
    part2 = search_marker(input, 14)

    return part1, part2

def search_marker(input, distinct_chars):
    for i in range(len(input)):
        cut = set(input[i:i+distinct_chars])
        if len(cut) == distinct_chars:
            return i+distinct_chars


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)