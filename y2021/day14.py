from lib.utils import read_input
from collections import defaultdict


def go():
    input = read_input("input/2021:14.txt", split_lines=True)

    # PART 1
    template = input.pop(0)
    # Remove the empty string from the array
    input.pop(0)

    mapping = dict([line.split(" -> ") for line in input])

    count = polymer_calc(template, mapping, 10)
    part1 = max(count) - min(count)

    pairs = defaultdict(int)
    elems = defaultdict(int)

    for i, char in enumerate(template[:-1]):
        pairs[template[i : i + 2]] += 1
        elems[char] += 1
    elems[template[-1]] += 1

    for _ in range(40):
        for comb, count in list(pairs.items()):
            new_elem = mapping.get(comb, "")
            elems[new_elem] += count
            pairs[comb] -= count
            pairs[comb[0] + new_elem] += count
            pairs[new_elem + comb[1]] += count

    part2 = max(elems.values()) - min(elems.values())

    return part1, part2


def polymer_calc(template, mapping, repetitions):
    for _ in range(repetitions):
        i = 0
        while True:
            chars = template[i : i + 2]
            if chars in mapping:
                template = template[: i + 1] + mapping[chars] + template[i + 1 :]
                i += 1
            i += 1
            if i == len(template):
                break
    return [(template.count(i)) for i in set(template)]


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2, sep="\n")
