def create_from_sequence(sequence: list) -> dict:
    """Create graph from degree sequence if possible

    Args:
        sequence (list): graph degree sequence

    Returns:
        dict: return graph in adjacency list form or empty dict if sequence was wrong
    """
    nodes_number = len(sequence)
    sequence.sort(reverse=True)
    if sequence[0] >= nodes_number or sequence[-1] < 0:
        return {}

    sequence = list(zip(range(nodes_number), sequence))
    graph = dict((i, list()) for i in range(nodes_number))

    while sequence[0][1] > 0:
        node, degree = sequence.pop(0)
        for i in range(degree):
            adj_node, adj_degree = sequence[i]
            if adj_degree < 1:
                return {}

            sequence[i] = (adj_node, adj_degree - 1)
            graph[node].append(adj_node)
            graph[adj_node].append(node)

        sequence.sort(key=lambda v: v[1], reverse=True)

    return graph
