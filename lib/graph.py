class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = {node: set() for node in range(self.size)}

    def add_edge(self, node1, node2, weight):
        self.graph[node1].add((node2, weight))

    def print_graph(self):
        for key in self.graph.keys():
            print("node", key, ": ", self.graph[key])