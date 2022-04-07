
# Grafo Simple No Dirigido con Lista de Adyacencia

class Graph:
    def __init__(self, nodes):
        self._nodes = nodes
        self._adj_list = {}

        for node in self._nodes:
            self._adj_list[node] = []

    def add_edge(self, u, v):               # O(1)
        self._adj_list[u].append(v)
        self._adj_list[v].append(u)

    def degree_vertex(self, node):          # O(1)
        degree = len(self._adj_list[node])
        return degree

    def print_adj(self):
        for node in self._nodes:
            print(node, ":", self._adj_list[node])


# Implementation Example

"""
nodes = ["A", "B", "C", "D", "E"]
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("B", "E"), ("C", "D"), ("D", "E")]
graph = Graph(nodes)
for u, v in edges:
    graph.add_edge(u, v)
graph.print_adj()

"""

