from lab3.graph_distance_matrix import graph_distance_matrix
from lab3.graph_generator import generate_connected_graph, generate_weights_matrix


def graph_centre_minimax(graph: dict, weights: list):
    """Function that returns graph centre and minimax centre

    Args:
        graph (dict): graph
        weights (list): graph weights
    """

    dist_matrix = graph_distance_matrix(graph, weights)

    center_calc = {}
    for k, i in enumerate(graph.keys()):
        center_calc[k] = (sum(dist_matrix[i]), max(dist_matrix[i]))

    center_vertex_num = max(center_calc, key=lambda x: center_calc[x][0])
    minimax_vertex_num = min(center_calc, key=lambda x: center_calc[x][1])

    center_vertices = list(filter(lambda x: center_calc[x][0]
                                  == center_calc[center_vertex_num][0], center_calc))

    minimax_vertices = list(filter(lambda x: center_calc[x][1]
                                   == center_calc[minimax_vertex_num][1], center_calc))

    return(center_vertices, minimax_vertices)


if __name__ == "__main__":
    graph = generate_connected_graph(5, 10)
    weights = generate_weights_matrix(graph, 1, 10)
    print(graph_centre_minimax(graph, weights))
