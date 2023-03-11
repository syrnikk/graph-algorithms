from random import randint, choice
from graphic_sequence import create_from_sequence
from graph_components import max_connected_components, depth_first_search


def generate_euler(n=-1):
    """Funkcja generujaca losowy graf Eulera

    Args:
        n (int, optional): ilosc wierzcholkow - w przypadku braku podania - wartosc losowa. Defaults to -1.

    Returns:
        _type_: wylosowany graf
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
    """Funkcja dodajaca krawedz miedzy u i v z powrotem

    Args:
        graph (dict): graf
        u (_type_): wierzcholek u
        v (_type_): wierzcholek v
    """

    graph[u].append(v)
    graph[v].append(u)


def remove_edge(graph : dict, u, v):
    """funkcja usuwajaca krawedz miedzy u i v

    Args:
        graph (dict): graf
        u (_type_): wierzcholek u
        v (_type_): wierzcholek v
    """

    graph[u].remove(v)
    graph[v].remove(u)


def is_bridge(graph : dict, u, v):
    """funkcja sprawdzajaca czy krawedz miedzy u i v jest mostem

    Args:
        graph (dict): graf
        u (_type_): wierzcholek u
        v (_type_): wierzcholek v

    Returns:
        bool : informacja czy krawedz (u,v) jest mostem
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
    """implementacja algorytmu Fleury'ego

    Args:
        graph (dict): graf

    Returns:
        list: lista odwiedzonych wierzcholkow
    """
    
    u = choice(list(graph.keys()))
    vertices_met = []

    def find_eulerian_trail(graph, u):
        for v in graph[u]:
            if not is_bridge(graph, u, v):
                vertices_met.append(u)
                remove_edge(graph, u, v)
                find_eulerian_trail(graph, v)

    find_eulerian_trail(graph, u)
    vertices_met.append(u)

    return vertices_met


if __name__ == "__main__":
    g = generate_euler(10)
    # g = {0: [1, 2, 3, 4], 1: [0, 2, 3, 4],
    #      2: [0, 1, 3, 6], 3: [0, 1, 2, 4], 4: [0, 1, 3, 5], 5: [4, 6], 6: [2, 5]} # przyklad z zajec
    print(g)
    res = fleury_algorithm(g)
    print(res)
