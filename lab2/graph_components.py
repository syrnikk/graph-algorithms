def depth_first_search(graph, start, visited=None):
    """Find list of strongly connected components including 'start' node

    Args:
        graph (dict): graph
        start (int): initial node index
        visited (list, optional): list of visited nodes. Defaults to None.

    Returns:
        list: list of strongly connected components
    """

    if visited is None:
        visited = set()
    visited.add(start)
    for next in set(graph[start]) - visited:
        depth_first_search(graph, next, visited)
    return visited


def find_connected_components(graph: dict):
    """Find connected components
    Args:
        graph (dict): graph

    Returns:
        list: list of strongly connected components
    """

    subgraphs = []
    nodes = list(graph.keys())
    while len(nodes) != 0:
        subgraph = depth_first_search(graph, nodes[0])
        subgraphs.append(subgraph)
        nodes = [node for node in nodes if node not in subgraph]
        graph = {key: value for key, value in graph.items() if key not in subgraph}

    return subgraphs


def max_connected_components(graph: dict):
    """Find max list of strongly connected components in graph

    Args:
        graph (dict): graph

    Returns:
        list: max list of strongly connected components
    """

    subgraphs = find_connected_components(graph)
    return max(subgraphs, key=len)
