from lib.utils import read_input


class Node:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def fold(self, num, x=False, y=False):
        if x:
            if self.x > num:
                self.x = num - (self.x - num)
        if y:
            if self.y > num:
                self.y = num - (self.y - num)


def go():
    input = read_input("input/2021:13.txt", split_lines=True)

    nodes = []
    while True:
        line = input.pop(0)
        # Don't process the fold instructions as coordinates
        if line == "":
            break
        x, y = line.split(",")
        nodes.append(Node(x, y))

    part1 = False
    for line in input:
        line = line.split(" ")[-1]
        axis, num = line.split("=")
        if axis == "x":
            fold(nodes, num=int(num), x=True)
        if axis == "y":
            fold(nodes, num=int(num), y=True)
        if not part1:
            part1 = len(set([(node.x, node.y) for node in nodes]))

    part2 = nodes_to_str(nodes)

    return part1, part2


def fold(nodes, num, x=False, y=False):
    for node in nodes:
        node.fold(num, x, y)


def nodes_to_str(nodes):
    nodes = list(set([(node.x, node.y) for node in nodes]))
    length = max([node[0] for node in nodes])
    height = max([node[1] for node in nodes])
    string = ""
    for y in range(height + 1):
        for x in range(length + 1):
            if nodes.count((x, y)):
                string += "#"
            else:
                string += "."
        string += "\n"
    string += "\n"
    return string


if __name__ == "__main__":
    part1, part2 = go()
    print(part1, part2, sep="\n")
