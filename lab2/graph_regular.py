from lab2.graphic_sequence import create_from_sequence
from lab2.graph_randomizer import randomly_swap_edges


def random_regular_graph(n, k):
    """Function creating random k-regular graph

    Args:
        n (int): number of vertices
        k (int): single vertex degree

    Returns:
        dict: k-regular graph
    """
    if n <= k or (k % 2 == 1 and n % 2 == 1):
        print("Invalid user input")
        return

    graph = create_from_sequence([k for _ in range(n)])

    randomly_swap_edges(graph, 100)

    return graph


if __name__ == "__main__":
    print(random_regular_graph(7, 2))
