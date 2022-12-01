from lib.utils import read_input

def go():

    input = read_input("input/2022:1.txt", split_lines=True)

    # PART 1

    calorie_counts = [0]
    for line in input:
        if line == '':
            calorie_counts.append(0)
        else:
            calorie_counts[-1] += int(line)

    part1 = (max(calorie_counts))

    # PART 2

    sorted_counts = sorted(calorie_counts, reverse=True)[:3]
    part2 = (sum(sorted_counts))

    return part1, part2


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)