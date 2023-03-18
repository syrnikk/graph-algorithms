import random
from lab1.graph_generator import generate_graph
from lab2.graph_components import find_connected_components
        
        
def generate_connected_graph(nodes_number, edges_number):
    """Function generating random connected graph

    Args:
        nodes_number (int): number of graph nodes
        edges_number (int): number of graph edges

    Raises:
        ValueError: raised when there is not enough edges to create connected graph

    Returns:
        dict: generated graph
    """
    if edges_number < nodes_number - 1:
        raise ValueError('There is no enough edges to create connected graph.')
    while True:
        graph = generate_graph(nodes_number, edges_number)
        if len(find_connected_components(graph)) == 1:
            break
    return graph


def generate_weights_matrix(graph: dict, min_weight, max_weight):
    """Function generating weights matrix for graph

    Args:
        graph (dict): graph
        min_weight (int): minimum weight
        max_weight (int): maximum weight

    Returns:
        list: generated weights matrix
    """
    weights_matrix = [[None for _ in graph] for _ in graph]
    for node, neighbours in graph.items():
        for neighbour in neighbours:
            if weights_matrix[node][neighbour] is None:
                weight = random.randint(min_weight, max_weight)
                weights_matrix[node][neighbour] = weight
                weights_matrix[neighbour][node] = weight
    return weights_matrix
