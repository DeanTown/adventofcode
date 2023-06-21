from lib.utils import read_input


class CRT:
    def __init__(self):
        self.cycle = 0
        self.pos = 0
        self.register = 1
        self.cycles = [20, 60, 100, 140, 180, 220]
        self.signal_strengths = []
        self.crt_string = ""


def go():
    input = read_input("input/2022:10.txt", split_lines=True)
    crt = CRT()
    for line in input:
        _, *addx = line.split()
        addx = addx[0] if addx else False
        # Both addx and noop need at least 1 cycle
        do_cycle(crt)
        if not addx:
            continue
        # addx needs an additional cycle and then the value is updated
        do_cycle(crt)
        # The value in the store is updated after the second cycle
        crt.register += int(addx)

    return sum(crt.signal_strengths), crt.crt_string


def do_cycle(crt):
    crt.cycle += 1
    if crt.cycle in crt.cycles:
        crt.signal_strengths.append(crt.cycle * crt.register)

    if abs(crt.pos - crt.register) > 1:
        print(".", end="")
        crt.crt_string += "."
    else:
        print("#", end="")
        crt.crt_string += "#"

    if crt.pos == 39:
        print()
        crt.pos = 0
    else:
        crt.pos += 1


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)
