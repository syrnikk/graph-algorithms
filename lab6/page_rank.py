import numpy as np
import random
from lab1.graph_converter import convert_list_to_matrix


def page_rank_random(digraph: dict, N: int):
    """Random walk page rank implementation

    Args:
        digraph (dict): digraph
        N (int): number of iterations

    Returns:
        list: List of tuples containing (node, pagerank value)
    """

    d = .15
    s = len(digraph)
    p = [0] * s

    random_node = random.choice(list(digraph.keys()))
    for _ in range(N):
        p[random_node] += 1

        probability = random.uniform(0, 1)

        if probability < d:
            random_node = random.choice(list(digraph.keys()))
        else:
            if len(digraph[random_node]) == 0:
                random_node = random.choice(list(digraph.keys()))
            else:
                random_node = random.choice(digraph[random_node])

    final_p = [(i, e / sum(p)) for i, e in enumerate(p)]

    return sorted(final_p, key=lambda x: x[1], reverse=True)


def page_rank_matrix(digraph: dict, eps: float = 1e-6):
    """Page rank implementation

    Args:
        digraph (dict): digraph
        eps (float, optional): epsilon. Defaults to 1e-6.

    Returns:
        list: List of tuples containing (node, pagerank value)
    """
    def vertices_degrees(digraph):
        return np.array([len(digraph[k]) for k in digraph])

    d = .15
    s = len(digraph)

    pt = [1/s] * s
    pt_1 = [0] * s

    P = np.zeros((s, s), dtype=float)

    A = convert_list_to_matrix(digraph)
    v = vertices_degrees(digraph)

    for i in range(s):
        for j in range(s):
            if v[i] != 0:
                P[i, j] = ((1-d)*A[i, j])/v[i] + d/s
            else:
                P[i, j] = 1/s
    while True:
        pt_1 = np.dot(pt, P)

        if np.linalg.norm(np.array(pt_1) - np.array(pt)) < eps:
            break

        pt = pt_1

    final_p = [(i, e) for i, e in enumerate(pt)]

    return sorted(final_p, key=lambda x: x[1], reverse=True)


def print_page_rank_pretty(page_rank_res: list):
    for entry, value in page_rank_res:
        print(f'{entry} ==> PageRank = {value:.6f}')


if __name__ == "__main__":
    g = {
        0: [4, 5, 8],
        1: [0, 2, 5],
        2: [1, 3, 4, 11],
        3: [2, 4, 7, 8, 10],
        4: [2, 6, 7, 8],
        5: [1, 6],
        6: [4, 5, 7],
        7: [3, 6, 8, 11],
        8: [3, 4, 7, 9],
        9: [8],
        10: [3, 8],
        11: [0, 7]
    }

    print("Random walk")
    print_page_rank_pretty(page_rank_random(g, 100000))

    print("Vector")
    print_page_rank_pretty(page_rank_matrix(g))
