import queue


def solve_flownet(graph: dict, s, t, tputs):
    flow_matrix = [[0 for _ in graph] for _ in graph]

    while True:
        residual_graph, residual_matrix = __generate_residual(
            graph, tputs, flow_matrix)

        path = __find_augmenting_path(residual_graph, s, t)

        if path is None:
            return [[None if v == 0 else v for v in line] for line in flow_matrix]

        flow_diff = __find_cost_over_path(path, residual_matrix)
        for i, j in zip(path, path[1:]):
            if j in graph[i]:
                flow_matrix[i][j] += flow_diff
            else:
                flow_matrix[i][j] -= flow_diff


def __generate_residual(graph: dict, tputs, flows):
    residual_matrix = [[None for _ in graph] for _ in graph]
    residual_graph = {node: [] for node in graph}

    for node, neighbours in graph.items():
        for neighbour in neighbours:
            tput = tputs[node][neighbour]
            flow = flows[node][neighbour]
            if flow > tput:
                raise AssertionError("Illegal: flow > tput")

            if flow < tput:
                residual_graph[node].append(neighbour)
                residual_matrix[node][neighbour] = tput - flow

            if flow > 0:
                residual_graph[neighbour].append(node)
                residual_matrix[neighbour][node] = flow

    return residual_graph, residual_matrix


def __find_augmenting_path(graph: dict, s, t):
    nodes_queue = queue.SimpleQueue()
    nodes_queue.put(s)
    previous = [None for _ in graph]
    while not nodes_queue.empty():
        node = nodes_queue.get()
        for neighbour in graph[node]:
            if previous[neighbour] is None:
                previous[neighbour] = node
                nodes_queue.put(neighbour)

            if neighbour == t:
                break

    path = [t]
    while path[-1] != s:
        node = previous[path[-1]]
        if node is None:
            return None

        path.append(node)

    path.reverse()
    return path


def __find_cost_over_path(path: list, residual):
    cost = residual[path[0]][path[1]]
    for i, j in zip(path, path[1:]):
        cost = min(cost, residual[i][j])

    return cost
