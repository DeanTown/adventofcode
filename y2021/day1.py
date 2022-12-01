from lib.utils import read_input

def go():

    input = read_input("input/2021:1.txt", split_lines=True)
    input = [int(measure) for measure in input]

    # PART 1

    prev_measure = input[0]
    increases = 0
    for measure in input[1:]:
        if measure > prev_measure:
            increases += 1
        prev_measure = measure

    part1 = increases

    # PART 2

    prev_measure_sum = sum(input[0:3])
    increases = 0
    for i in range(1, len(input)):
        if i+3 > len(input):
            break
        measure_sum = sum(input[i:i+3])
        if measure_sum > prev_measure_sum:
            increases += 1
        prev_measure_sum = measure_sum

    part2 = increases

    return part1, part2


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)