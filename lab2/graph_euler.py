from random import randint, choice
from graphic_sequence import create_from_sequence
from graph_components import max_connected_components, depth_first_search


def generate_euler(n=-1):
    """Function generating random Euler graph

    Args:
        n (int, optional): number of vertices - in case of missing the parameter - random value. Defaults to -1.

    Returns:
        dict: random Euler graph
    """

    if n == -1:
        n = randint(2, 10)
    elif n == 2:
        # specjalny przypadek
        return {0: [1], 1: [0]}
    
    graph = {}
    while graph == {}:
        seq = [randint(1, n//2)*2 for _ in range(n)]
        graph = create_from_sequence(seq)

    connected_vertices = max_connected_components(graph)

    euler_graph = {k: graph[k]
                             for k in connected_vertices if k in graph}
    graph = euler_graph
    
    return graph


def add_edge_back(graph : dict, u, v):
    """Function that adds edge between u and v

    Args:
        graph (dict): graph
        u (int): vertex u
        v (int): vertex v
    """

    graph[u].append(v)
    graph[v].append(u)


def remove_edge(graph : dict, u, v):
    """Function removing edge between u and v

    Args:
        graph (dict): graph
        u (int): vertex u
        v (int): vertex v
    """

    graph[u].remove(v)
    graph[v].remove(u)


def is_bridge(graph : dict, u, v):
    """Function checking whether edge between u and v is a bridge

    Args:
        graph (dict): graph
        u (int): vertex u
        v (int): vertex v

    Returns:
        bool : is (u,v) bridge 
    """

    if len(graph[u]) == 1:
        return False
    else:
        count_before_removal = len(depth_first_search(graph, u))
        remove_edge(graph, u, v)
        count_after_removal = len(depth_first_search(graph, u))
        add_edge_back(graph, u, v)
        return count_before_removal > count_after_removal


def fleury_algorithm(graph : dict):
    """Fleury's algorithm implementation

    Args:
        graph (dict): graph

    Returns:
        list: visited vertices
    """
    
    u = choice(list(graph.keys()))
    visited_vertices = []

    def find_eulerian_trail(graph, u):
        for v in graph[u]:
            if not is_bridge(graph, u, v):
                visited_vertices.append(u)
                remove_edge(graph, u, v)
                find_eulerian_trail(graph, v)

    find_eulerian_trail(graph, u)
    visited_vertices.append(u)

    return visited_vertices


if __name__ == "__main__":
    g = generate_euler(10)
    # g = {0: [1, 2, 3, 4], 1: [0, 2, 3, 4],
    #      2: [0, 1, 3, 6], 3: [0, 1, 2, 4], 4: [0, 1, 3, 5], 5: [4, 6], 6: [2, 5]} # przyklad z zajec
    print(g)
    res = fleury_algorithm(g)
    print(res)
