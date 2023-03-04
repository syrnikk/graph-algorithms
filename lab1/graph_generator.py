import random
import itertools


def generate_graph(nodes_number, edges_number):
    """Function generating random graph by nodes and edges number"""
    if edges_number < 0 or edges_number > nodes_number * (nodes_number - 1) / 2:
        raise ValueError('Incorrect edges number.')
    nodes = list(range(nodes_number))
    neighbours = [[] for _ in range(nodes_number)]
    edges = random.sample(list(itertools.combinations(nodes, 2)), edges_number)
    for first_node, second_node in edges:
        neighbours[first_node].append(second_node)
        neighbours[second_node].append(first_node)
    return dict(zip(nodes, neighbours))


def generate_graph_by_probability(nodes_number, edge_probability):
    """Function generating random graph by nodes number and edge probability"""
    if edge_probability < 0 or edge_probability > 1:
        raise ValueError('Incorrect edge probability.')
    nodes = list(range(nodes_number))
    neighbours = [[] for _ in range(nodes_number)]
    edges = itertools.combinations(nodes, 2)
    for first_node, second_node in edges:
        if random.random() < edge_probability:
            neighbours[first_node].append(second_node)
            neighbours[second_node].append(first_node)
    return dict(zip(nodes, neighbours))
