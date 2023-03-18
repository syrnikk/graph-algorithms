import lab3.graph_generator
import itertools
import copy


def find_min_spanning_tree(graph: dict, weights: list):
    """Find and return minimal spanning tree of graph using Prim alghoritm

    Args:
        graph (dict): graph to find spanning tree
        weights (list): matrix of edges weights in list of lists form

    Raises:
        ValueError: raised if graph occurs to be disconnected

    Returns:
        dict: spanning tree of provided graph
    """
    spanning_tree = {}
    graph = copy.deepcopy(graph)

    node, neighbours = graph.popitem()
    connecting_edges = set(zip(itertools.cycle([node]), neighbours))
    spanning_tree.setdefault(node, list())

    # remove connecting edges from graph
    for neighbour in neighbours:
        graph[neighbour].remove(node)

    while connecting_edges:
        # find edge with lowest cost
        light_edge = min(connecting_edges,
                         key=lambda edge: weights[edge[0]][edge[1]])
        if light_edge[0] not in spanning_tree:
            light_edge = (light_edge[1], light_edge[0])

        # remove edges to new spanning tree node
        connecting_edges -= set(zip(spanning_tree,
                                itertools.cycle([light_edge[1]])))

        # add connecting edges from new spanning tree node
        node = light_edge[1]
        neighbours = graph.pop(node)
        connecting_edges |= set(zip(itertools.cycle([node]), neighbours))

        # remove connecting edges from graph
        for neighbour in neighbours:
            graph[neighbour].remove(node)

        # add new node and edge to spanning tree
        spanning_tree[light_edge[0]].append(light_edge[1])
        spanning_tree.setdefault(light_edge[1], [light_edge[0]])

    if graph:
        raise ValueError("Provided graph is not connected.")

    return spanning_tree

