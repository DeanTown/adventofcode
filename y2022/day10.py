from lib.utils import read_input

signal_strengths = []
cycles = [20, 60, 100, 140, 180, 220]


def go():
    input = read_input("input/2022:10.txt", split_lines=True)
    # PART 1
    cycle = 0
    value = 1
    for line in input:
        _, *addx = line.split()
        addx = addx[0] if addx else False
        # Both addx and noop need at least 1 cycle
        cycle += 1
        check_cycle(cycle, value)
        if not addx:
            continue
        # addx needs an additional cycle and then the value is updated
        cycle += 1
        check_cycle(cycle, value)
        # The value in the store is updated after the second cycle
        value += int(addx)

    part1 = sum(signal_strengths)
    return part1, 2


def check_cycle(cycle, value):
    if cycle in cycles:
        signal_strengths.append(cycle * value)


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)
