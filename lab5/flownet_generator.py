import itertools
import random
from random import randint


def generate_flownet(hidden_layers: int, edge_min_weight: int = 1, edge_max_weight: int = 10):
    if hidden_layers < 2:
        raise ValueError('Incorrect number of nodes')

    # first layer
    graph = {0: []}
    layers = {0: [0]}

    # hidden layers
    for i in range(1, hidden_layers + 1):
        layer_i_nodes = randint(2, hidden_layers)
        max_node = max(graph)

        # insert vertexes in graph
        graph.update({node: [] for node in range(max_node + 1, max_node + layer_i_nodes + 1)})

        # add graph layer
        layers[i] = list(range(max_node + 1, max_node + layer_i_nodes + 1))

    # last layer
    graph[max(graph) + 1] = []
    layers[hidden_layers + 1] = [max(graph)]

    ###
    # add edges between layers
    ###

    # first layer
    graph[0] = layers[1].copy()

    # hidden and last layers
    for i in range(1, hidden_layers + 1):
        for node in layers[i + 1]:
            graph[random.choice(layers[i])].append(node)

        for node in layers[i]:
            edge_to = random.choice(layers[i + 1])
            if len(graph[node]) == 0:
                graph[node].append(edge_to)

    # additional 2n edges
    all_candidates = []
    for i in range(1, hidden_layers):
        all_candidates += list(itertools.product(layers[i], layers[i + 1])) + list(
            itertools.product(layers[i + 1], layers[i]))

    chosen_candidates = random.choices(all_candidates, k=2 * hidden_layers)

    for candidate in chosen_candidates:
        if candidate[0] not in graph[candidate[1]] and candidate[1] not in graph[candidate[0]]:
            graph[candidate[0]].append(candidate[1])

    return graph, layers, __generate_weights_matrix(graph, edge_min_weight, edge_max_weight)


def __generate_weights_matrix(graph: dict, min_weight, max_weight):
    weights_matrix = [[None for _ in graph] for _ in graph]
    for node, neighbours in graph.items():
        for neighbour in neighbours:
            if weights_matrix[node][neighbour] is None:
                weight = random.randint(min_weight, max_weight)
                weights_matrix[node][neighbour] = weight
    return weights_matrix
