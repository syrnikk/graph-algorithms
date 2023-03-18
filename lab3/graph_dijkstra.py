import math
from lab3.graph_generator import generate_connected_graph, generate_weights_matrix


class GraphDijkstra:
    def __init__(self, graph, weights_matrix, source_node) -> None:
        # ds[u] the length of the shortest path s → u
        self.ds = {node: math.inf for node in graph}
        # ps[u] antecedent of node u on the shortest path s → u
        self.ps = {node: None for node in graph}
        self.source_node = source_node
        self.ds[source_node] = 0

        # a set of "ready" nodes
        s = set()
        all_nodes = set(graph.keys())
        while len(all_nodes.difference(s)) != 0:
            # node with the smallest ds[u] value from 'not ready' nodes
            u = min([(i, val) for i, val in self.ds.items() if i not in s], key=lambda pair: pair[1])[0]
            s.add(u)
            for v in graph[u]:
                if v not in s:
                    self.__relax(u, v, weights_matrix)

    def print_shortest_paths(self):
        for node in self.ds:
            path = []
            next_node = node
            while next_node is not None:
                path.insert(0, next_node)
                next_node = self.ps[next_node]
            print(f'{self.source_node} -> {node}: {path}')

    def __relax(self, u, v, weights_matrix):
        if self.ds[v] > self.ds[u] + weights_matrix[u][v]:
            self.ds[v] = self.ds[u] + weights_matrix[u][v]
            self.ps[v] = u


if __name__ == '__main__':
    graph = generate_connected_graph(20, 40)
    weights = generate_weights_matrix(graph, 1, 10)
    alg = GraphDijkstra(graph, weights, 0)
    alg.print_shortest_paths()
