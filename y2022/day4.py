from lib.utils import read_input

def go():

    input = read_input("input/2022:4.txt", split_lines=True)
    pairs = [[[int(num) for num in pair.split('-')] for pair in line.split(',')] for line in input]

    part1 = find_overlaps(pairs)
    part2 = find_overlaps(pairs, any_overlap=True)

    return part1, part2

"""
If one range fully encloses another, then the intersection between them will equal one of the two ranges.
If one range partially overlaps another, then the intersection will have at least 1 value.
"""
def find_overlaps(pairs, any_overlap=False):
    overlap = 0
    for first, second in pairs:
        first = set(range(first[0], first[1]+1))
        second = set(range(second[0], second[1]+1))
        intersection = first & second
        if intersection == second or intersection == first: overlap += 1
        elif any_overlap and len(intersection) > 0: overlap += 1
    return overlap


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)