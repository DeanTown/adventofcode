"""
Think about it like it's a numbered grid, and instead of caring about the data structure, just calculate the positions based on the rules and keep a list of visited locations

5
4
3 A   B
2
1   
0 
  0 1 2 3 4 5

(0,0) is the starting coordinate
If we move 3 up:
A=(0,3)
If we move 2 right
B=(2,3)
This solution will work for any size grid as well as negatives in both directions
"""

from lib.utils import read_input


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Grid:
    def __init__(self):
        self.head = Point(0, 0)
        self.tail = Point(0, 0)
        self.visited_nodes = set()

    def move_head(self, direction, distance):
        if direction in ["D", "L"]:
            distance *= -1
        if direction in ["U", "D"]:
            self.head = Point(self.head.x, self.head.y + distance)
        else:
            self.head = Point(self.head.x + distance, self.head.y)

    def calculate_diff(self):
        diff = self.head - self.tail

        if not diff.x == 0 and not diff.y == 0:
            return diff
        vector = Point(0, 0)
        if abs(diff.x) > 1:
            vector.x = 1 if diff.x > 0 else -1
        if abs(diff.y) > 1:
            vector.y = 1 if diff.y > 0 else -1
        return vector


def go():
    input = read_input("input/2022:9.txt", split_lines=True)
    grid = Grid()

    for line in input:
        direction, distance = line.split()
        for _ in range(int(distance)):
            grid.move_head(direction, 1)
            # We can use the difference between the head and tail of the grid to determine what movement is required
            diff = grid.calculate_diff()
            grid.tail += diff
            grid.visited_nodes.add(grid.tail)

    return len(grid.visited_nodes), 2


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)
