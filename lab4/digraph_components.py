from lab4.digraph_generator import generate_digraph_by_probability
from matplotlib import pyplot as plt
import igraph


def find_connected_components(graph: dict):
    stack = []
    visited = [False] * len(graph)
    for node, neighbors in graph.items():
        if not visited[node]:
            __depth_first_search(graph, node, visited, stack)

    transposed_graph = __transpose(graph)

    visited = [False] * len(graph)

    connected_components = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            __depth_first_search(transposed_graph, node, visited, component)
            connected_components.append(component)

    return connected_components


def __depth_first_search(graph: dict, node: int, visited: list, stack: list):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            __depth_first_search(graph, neighbor, visited, stack)
    stack.append(node)


def __transpose(graph):
    transposed_graph = {v: [] for v in graph}
    for u, edges in graph.items():
        for v in edges:
            transposed_graph[v].append(u)
    return transposed_graph


if __name__ == '__main__':
    graph = generate_digraph_by_probability(5, 0.3)
    print(find_connected_components(graph))

    # plot
    fig, ax = plt.subplots(figsize=(5, 5))

    g = igraph.Graph(directed=True)
    g.add_vertices(list(range(len(graph))))
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            g.add_edge(vertex, neighbor)
    igraph.plot(g, target=ax, vertex_label=graph.keys(), vertex_color='Dark Olive Green', edge_width=2,
                background='Light Slate Gray')

    plt.show()
