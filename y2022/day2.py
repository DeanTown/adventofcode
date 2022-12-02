from lib.utils import read_input

def go():

    input = read_input("input/2022:2.txt", split_lines=True)
    """
        Rock: 1, Paper: 2, Scissors: 3
        Win: 6, Draw: 3, Lose: 0,
        A: Rock, B: Paper, C: Scissors
        Part 1:
            X: Rock, Y: Paper, Z: Scissors
        Part 2:
            X: Lose, Y: Draw, Z: Win
    """
    map = {
        ('A', 'X'): (4, 3),
        ('A', 'Y'): (8, 4),
        ('A', 'Z'): (3, 8),
        ('B', 'X'): (1, 1),
        ('B', 'Y'): (5, 5),
        ('B', 'Z'): (9, 9),
        ('C', 'X'): (7, 2),
        ('C', 'Y'): (2, 6),
        ('C', 'Z'): (6, 7),
    }
    part1 = 0
    part2 = 0
    for line in input:
        opponent, you = line.split(' ')
        map_values = map[(opponent, you)]
        part1 += map_values[0]
        part2 += map_values[1]
    return part1, part2


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)