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
        return (self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Rope:
    def __init__(self):
        self.head = Point(0, 0)
        self.tail = Point(0, 0)
        self.visited_nodes = {}

    def move_head(self, direction, distance):
        if direction in ['D', 'L']:
            distance *= -1

        if direction in ['U', 'D']:
            self.head = Point(self.head.y, self.head.y + distance)
        else:
            self.head = Point(self.head.y + distance, self.head.y)

        return self.head


def go():

    input = read_input("input/2022:9.txt", split_lines=True)
    rope = Rope()

    for line in input:
        direction, distance = line.split()
        for dist in range(int(distance)):
            head = rope.move_head(direction, 1)
            # We can use the difference between the head and tail of the rope to determine what movement is required
            diff = head - rope.tail
            
        

    return 1,2


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2)