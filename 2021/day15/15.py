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
"""
for i in range(input_len):
    directions = [i-line_len, i+line_len, i-1, i+1]
    for dir in directions:
        if dir >=0 and dir < input_len:
            graph.add_edge(dir, i, int(input[i]))

graph.print_graph()
        