from lib.utils import read_input

class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False

    def __repr__(self):
        return str(self.value)

def go():

    input = read_input("input/2022:8.txt", split_lines=True)
    trees = [[Node(int(char)) for char in line] for line in input]

    west = trees
    east = [list(reversed(line)) for line in west]
    north = [[line[i] for line in trees] for i in range(len(trees[0]))]
    south = [list(reversed(line)) for line in north]

    sightlines = [north, south, east, west]

    visible = 0
    for direction in sightlines:
        for line in direction:
            tallest = Node(-1)
            for tree in line:
                if tallest.value < tree.value:
                    if not tree.visited: visible += 1
                    tree.visited = True
                    tallest = tree

    return visible, 2


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)