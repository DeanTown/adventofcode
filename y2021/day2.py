from lib.utils import read_input

def go():

    input = read_input("input/2021:2.txt", split_lines=True)

    # PART 1

    horizontal_pos = 0
    depth_pos = 0
    for dir in input:
        direction, distance = dir.split(' ')
        distance = int(distance)
        if direction == 'forward':
            horizontal_pos += distance
        elif direction == 'up':
            depth_pos -= distance
        elif direction == 'down':
            depth_pos += distance

    part1 = depth_pos * horizontal_pos

    # PART 2

    horizontal_pos = 0
    depth_pos = 0
    aim = 0
    for dir in input:
        direction, distance = dir.split(' ')
        distance = int(distance)
        if direction == 'forward':
            horizontal_pos += distance
            depth_pos += aim * distance
        elif direction == 'up':
            aim -= distance
        elif direction == 'down':
            aim += distance

    part2 = depth_pos * horizontal_pos

    return part1, part2


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)