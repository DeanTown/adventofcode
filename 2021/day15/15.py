from lib.utils import read_input
from lib.graph import Graph

input = read_input("2021/day15/input.txt")
# We will need both the individual lines as well as the whole string of numbers
lines = input.split('\n')
input = input.replace('\n', '')
line_len = len(lines[0])
input_len = len(input)

graph = Graph(input_len)

"""
Convert the input into an adjacency list

Reqs:
    1. The absolute position of each neighboring node from the input file
    2. Whether the neighboring nodes exist, i.e. if the current node is on an edge where it might only have 2 or 3 neighbors
    3. The weight of the current node which affects incoming edges
"""
for line_index, line in enumerate(lines):
    for char_index, weight in enumerate(line):
        dirs = [
            
        ]
        neighbors = []
        neighbors = [
            lines[line_index-1][char_index],
            lines[line_index+1][char_index],
            line[char_index-1],
            line[char_index+1],
        ]
        neighbors = {
            line_index-1,
            line_index+1,
            char_index-1,
            char_index+1,
        }


for i in range(input_len):
    directions = [i-line_len, i+line_len, i-1, i+1]
    for dir in directions:
        if dir >= 0 and dir < input_len:
            graph.add_edge(dir, i, int(input[i]))

graph.print_graph()
        