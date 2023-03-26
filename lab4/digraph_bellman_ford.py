import math
from lab4.digraph_generator import generate_digraph_by_probability
from lab4.digraph_components import find_connected_components
from lab3.graph_generator import generate_weights_matrix
import random
import igraph
import matplotlib.pyplot as plt


def __change_node_labels(graph: dict):
    new_graph = {}
    old_keys = list(graph.keys())
    for i in range(len(old_keys)):
        new_graph[i] = graph[old_keys[i]]

    return new_graph

def __generate_random_connected_digraph(max_node_number: int):
    if max_node_number < 3:
        raise ValueError("Maximum node number must be greater than 3")

    nodes_number = random.randint(3, max_node_number)
    probability = random.uniform(0.2, 1)

    connected_random_digraph = {}

    while len(connected_random_digraph.keys()) <= nodes_number - 1:
        random_digraph = generate_digraph_by_probability(
            nodes_number, probability)
        components = find_connected_components(random_digraph)
        max_component_len = max(map(lambda x: len(x), components))

        max_component = list(filter(lambda x: len(
            x) == max_component_len, components))[0]

        connected_random_digraph = {
            k: v for k, v in random_digraph.items() if k in max_component}

    connected_random_digraph = __change_node_labels(connected_random_digraph)

    return connected_random_digraph


def __assign_edge_weight(digraph: dict, min_weight: int, max_weight: int):
    if min_weight > max_weight:
        raise ValueError(
            "Minimum weight cannot be greater than maximum weight")

    weights_matrix = generate_weights_matrix(digraph, min_weight, max_weight)

    return (digraph, weights_matrix)


def bellman_ford(graph: dict, weights: list, start: int):
    if start > len(graph.keys()):
        raise ValueError("Starting vertex not present in the graph")

    def init(source_node):
        ds = {node: math.inf for node in graph}
        ps = {node: None for node in graph}
        
        ds[source_node] = 0

        return (ds,ps)

    def relax(ds, ps, u, v, weights):
        if ds[v] > ds[u] + weights[u][v]:
            ds[v] = ds[u] + weights[u][v]
            ps[v] = u

    def print_shortest_path(ps):
        for k in reversed(graph.keys()):
            c = k
            while c != None:
                print(c,end = '->')
                c = ps[c]
            print('None',end = '')
            print()

    (ds,ps) = init(start)
    n = len(graph.keys())

    for _ in range(n-1):
        for u,n in graph.items():
            for v in n:
                relax(ds, ps ,u, v, weights)
    
    for u,n in graph.items():
        for v in n:
            if ds[v] > ds[u] + weights[u][v]:
                raise ValueError("Graph contains negative cycle")
    
    print_shortest_path(ps)

if __name__ == "__main__":
    g = __generate_random_connected_digraph(5)
    g, w = __assign_edge_weight(g, -2, 100)

    bellman_ford(g,w,0)

    fig, ax = plt.subplots(figsize=(5, 5))

    gr = igraph.Graph(directed = True)
    gr.add_vertices(list(g.keys()))

    for u,n in g.items():
        for v in n:
            if w[u][v] != None:
                gr.add_edge(u,v,weight = w[u][v])

    gr.es['weight'] = [e['weight'] for e in gr.es]
    layout = gr.layout("kk")

    igraph.plot(gr, target=ax, layout = layout, vertex_label = g.keys() ,edge_label = gr.es['weight'])

    plt.show()

