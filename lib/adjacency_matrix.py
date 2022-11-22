class GraphAM:
    def __init__(self, size):
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, v1, v2, weight):
        # You should not be able to add an edge between a vertex and itself
        if v1 == v2:
            return False
        self.matrix[v1][v2] = weight
        self.matrix[v2][v1] = weight

    def remove_edge(self, v1, v2):
        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0
