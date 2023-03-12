import random
import numpy as np
from lab1 import graph_converter


def randomly_swap_edges(graph: dict, swaps_num=5, max_total_attempts=1000) -> dict:
    """Randomize graph in place by swapping edges {a, b}, {c, d} to {a, d}, {b, c} swaps_num times

    Args:
        graph (dict): graph in adjacency list form
        swaps_num (int, optional): number of edges swaps. Defaults to 5.
        max_total_attempts (int, optional): max of total attempts to swap edges. Defaults to 1000.

    Returns:
        dict: randomized graph in adjacency list form
    """

    def is_not_legal_to_add_edge(edge):
        return edge[0] == edge[1] or edge[1] in graph[edge[0]] or edge[0] in graph[edge[1]]

    def remove_edge(edge):
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])

    def add_edge(edge):
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    non_zeros = iter(np.nonzero(
        graph_converter.convert_list_to_incidence(graph).T)[1])
    edges = list(zip(non_zeros, non_zeros))
    nof_edges = len(edges)
    swaps_left = swaps_num
    attempts = 0
    while swaps_left > 0:
        if attempts >= max_total_attempts:
            print(
                "Too many attempts, graph is dense so it's hard to randomly find proper edges to swap, returning "
                "graph with", swaps_num - swaps_left, "swaps done")
            return graph

        attempts += 1
        indexes = random.sample(range(nof_edges), 2)
        ab = edges[indexes[0]]
        cd = edges[indexes[1]]

        ad = (ab[0], cd[1])
        bc = (ab[1], cd[0])

        if is_not_legal_to_add_edge(ad) or is_not_legal_to_add_edge(bc):
            continue

        remove_edge(ab)
        remove_edge(cd)
        add_edge(ad)
        add_edge(bc)

        edges[indexes[0]] = ad
        edges[indexes[1]] = bc

        swaps_left -= 1
