def find_hamilton_path(graph):
    nodes = list(graph.keys())

    for node in nodes:
        path = __hamilton_path_rec(graph, node)
        if path:
            return path

    return None


def __hamilton_path_rec(graph, node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)

    if __is_hamilton_path_found(graph, visited):
        return __append_root_node(visited)

    for neighbour in graph[node]:
        if not visited.count(neighbour):
            path = __hamilton_path_rec(graph, neighbour, visited)

            if path:
                return path

    visited.remove(node)


def __is_hamilton_path_found(graph, path):
    nodes = list(graph.keys())
    root_node = path[0]
    tail_node = path[-1]
    return len(path) == len(nodes) and graph[tail_node].count(root_node)


def __append_root_node(path):
    root_node = path[0]
    path_c = path.copy()
    path_c.append(root_node)
    return path_c
