import itertools
from random import random


def generate_digraph_by_probability(nodes_number, edge_probability):
    """Function generating random graph by nodes number and edge probability"""
    if edge_probability < 0 or edge_probability > 1:
        raise ValueError('Incorrect edge probability.')
    nodes = list(range(nodes_number))
    neighbours = [[] for _ in range(nodes_number)]
    edges = itertools.permutations(nodes, 2)
    for first_node, second_node in edges:
        if random() < edge_probability:
            neighbours[first_node].append(second_node)
    return dict(zip(nodes, neighbours))
