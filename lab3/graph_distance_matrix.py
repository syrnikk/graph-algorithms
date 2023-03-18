import lab3.graph_dijkstra as gd


def graph_distance_matrix(graph, weights_matrix):
    """Return graph distance matrix

    Args:
        graph (dict): graph representation
        weights_matrix (list): weights matrix

    Returns:
        list: distance matrix
    """
    distance_matrix = []
    for node in graph:
        alg = gd.GraphDijkstra(graph, weights_matrix, node)
        distance_matrix.append(list(alg.ds.values()))
    return distance_matrix
