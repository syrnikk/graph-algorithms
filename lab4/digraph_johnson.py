import math
from copy import deepcopy
from itertools import product

from lab4.digraph_bellman_ford import bellman_ford


def johnson(graph: dict, weights: list):
    graph_prim, weights_prim = __add_s(graph, weights)

    ds, ps = bellman_ford(graph_prim, weights_prim, len(graph_prim) - 1)

    for u, v in product(range(len(graph)), repeat=2):
        if weights_prim[u][v] is not None:
            weights_prim[u][v] += ds[u] - ds[v]

    d = [[0] * len(graph) for i in range(len(graph))]

    for u in range(len(graph)):
        ds_d, ps_d = __dijkstra(graph, weights_prim, u)
        for v in range(len(graph)):
            d[u][v] = ds_d[v] - ds[u] + ds[v]

            if d[u][v] == math.inf:
                d[u][v] = None

    return d


def __add_s(graph: dict, weights: list):
    graph_prim = deepcopy(graph)
    weights_prim = deepcopy(weights)

    for i in range(len(graph)):
        weights_prim[i].append(0)
    weights_prim.append([0] * len(graph_prim))
    weights_prim[-1].append(None)

    graph_prim[len(graph_prim)] = list(range(0, len(graph_prim)))

    return graph_prim, weights_prim


def __dijkstra(graph: dict, weights: list, s: int):
    n = len(graph)
    ds = [math.inf] * n
    ds[s] = 0
    ps = [None] * n
    q = list(range(n))

    while len(q) > 0:
        u = min(q, key=lambda x: ds[x])
        q.remove(u)

        for v in graph[u]:
            if ds[v] > ds[u] + weights[u][v]:
                ds[v] = ds[u] + weights[u][v]
                ps[v] = u

    return ds, ps
