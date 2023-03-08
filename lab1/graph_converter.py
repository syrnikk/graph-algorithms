import numpy as np


def convert_list_to_matrix(graph_list: dict, nodes_number):
    """Funciont converting graph storage form from adjacency list to adjacency matrix"""
    graph_matrix = np.zeros((nodes_number, nodes_number), np.uint8)
    for node, neighbours in graph_list.items():
        for neighbour in neighbours:
            graph_matrix[node][neighbour] = 1

    return graph_matrix


def convert_matrix_to_list(graph_matrix: np.matrix, nodes_number):
    """Funciont converting graph storage form from adjacency matrix to adjacency list"""
    graph_list = dict((i, list()) for i in range(nodes_number))
    for i in range(nodes_number):
        for j in range(nodes_number):
            if graph_matrix[i, j] > 0:
                graph_list[i].append(j)

    return graph_list


def convert_list_to_incidence(graph_list: dict, nodes_number):
    """Funciont converting graph storage form from adjacency list to incidence matrix"""
    edges_number = 0
    graph_incidence_T = np.zeros((0, nodes_number), np.uint8)
    for node, neighbours in graph_list.items():
        for neighbour in neighbours:
            new = np.zeros((1, nodes_number), np.uint8)
            new[0, node] = 1
            new[0, neighbour] = 1

            def already_inserted():
                for row in graph_incidence_T:
                    if (row == new[0]).all():
                        return True
                return False

            if not already_inserted():
                graph_incidence_T = np.append(graph_incidence_T, new, axis=0)

    return graph_incidence_T.T


def convert_incidence_to_list(graph_incidence: np.matrix):
    """Funciont converting graph storage form from incidence matrix to adjacency list"""
    nodes_number = graph_incidence.shape[0]
    graph_list = dict((i, list()) for i in range(nodes_number))
    it = iter(np.nonzero(graph_incidence.T)[1])
    for i, j in zip(it, it):
        graph_list[i].append(j)
        graph_list[j].append(i)

    return graph_list
