import csv

def read_list(src, v_sep=":", n_sep=","):
    """Function that reads graph represented as list

    Args:
        src (string): string value of graph represented as list 
        v_sep (str, optional): separator for vertices. Defaults to ":".
        n_sep (str, optional): separator for neighbors. Defaults to ",".

    Returns:
        dictionary: graph represented as list
    """

    data = csv.DictReader(src, delimiter=n_sep, fieldnames=[])
    result = []
    for d in data.reader:
        h = d[0].split(v_sep)
        result.append((h[0], [h[1], *d[1:]]))

    return dict(result)


def read_adj_matrix(src, no_v=False, no_e=False, v_sep=" ", e_sep=" ", a_sep=","):
    """Function that reads graph represented as adjacency matrix

    Args:
        src (string): string value of graph represented as adjacency matrix
        no_v (bool, optional): no vertices labels. Defaults to False.
        no_e (bool, optional): no edges labels. Defaults to False.
        v_sep (str, optional): vertices separator. Defaults to " ".
        e_sep (str, optional): edges separator. Defaults to " ".
        a_sep (str, optional): separator. Defaults to ",".

    Returns:
        tuple: tuple containing (vertices, edges, matrix)
    """

    data = csv.DictReader(src, delimiter=a_sep, fieldnames=[])
    vertices = []
    edges = []

    matrix = []
    for i, d in enumerate(data.reader):
        if not no_e and i == 0:
            edges = d[1::][0].split(e_sep)
            continue

        if not no_v and (i > 0 if not no_e else i > -1):
            h = d[0].split(v_sep)
            vertices.append(h[0])
            matrix.append([int(h[1]), *map(lambda x:int(x), d[1:])])
        else:
            matrix.append(list(map(lambda x:int(x),d)))
    return (vertices, edges, matrix)


def read_nei_matrix(src, no_v=False, v_sep=" ", n_sep=","):
    """Function that reads graph represented as neighbor matrix

    Args:
        src (string): string value of graph represented as neighbor matrix 
        no_v (bool, optional): no vertices labels. Defaults to False.
        v_sep (str, optional): vertices separator. Defaults to " ".
        n_sep (str, optional): neighbors separator. Defaults to ",".

    Returns:
        tuple: tuple containing (vertices, matrix)
    """

    data = list(map(lambda x: x[:-1], src))

    vertices = [str(i+1) for i in range(len(data))] if no_v else data[0].split(v_sep)

    matrix = list(map(lambda x: x.split(n_sep), data[0 if no_v else 1:]))
    
    return (vertices, matrix)


def print_list(list):
    """Function printing the graph from the list form

    Args:
        list (dictionary): list representation of the graph
    """

    for k, v in list.items():
        print(k, end=": ")
        print(",".join(v))


def print_nei_matrix(vertices, matrix, sep=" ", display_dashes=True):
    """Function printing the graph from the neighbor matrix form

    Args:
        vertices (list): list of vertices
        matrix (2d-list): neighbor matrix
        sep (str, optional): printing separator. Defaults to " ".
        display_dashes (bool, optional): displays row of dashes between labels and matrix contents if set to True. Defaults to True.

    Raises:
        ValueError: Lengths do not match
    """

    if len(vertices) != len(matrix[0]):
        raise ValueError("Lengths do not match")
    print(sep.join(vertices))

    if display_dashes:
        print(sep.join(["-" for _ in range(len(vertices))]))

    for r in matrix:
        for c in r:
            print(c, end=sep)
        print()


def print_adj_matrix(vertices, edges, matrix, sep=" "):
    """Function printing the graph from the adjacency matrix form

    Args:
        vertices (list): list of vertices
        edges (list): list of edges
        matrix (2d-list): adjacency matrix
        sep (str, optional): printing separator. Defaults to " ".
    """

    print(f'{sep}{sep.join(edges)}')
    for i, r in enumerate(matrix):
        if len(vertices) > 0:
            print(vertices[i], end=sep)
        for c in r:
            print(c, end=sep)
        print()


if __name__ == "__main__":
    with open("./examples/list.txt", "r") as f:
        li = read_list(f, v_sep=";", n_sep=",")
        print_list(li)
        print()
    with open("./examples/nei_matrix.txt", "r") as f:
        mt = read_nei_matrix(f.readlines(), v_sep=" ", n_sep=" ")
        print_nei_matrix(mt[0], mt[1])
        print()
    with open("./examples/adj_matrix.txt", "r") as f:
        adj = read_adj_matrix(f, v_sep=";", e_sep="f", a_sep=" ")
        print_adj_matrix(adj[0], adj[1], adj[2])
        print()
    with open("./examples/adj_matrix_no_header.txt", "r") as f:
        adj = read_adj_matrix(f, no_e=True, v_sep="x", a_sep=" ")
        print_adj_matrix(adj[0], adj[1], adj[2])
        print()
    with open("./examples/adj_matrix_no_edges_vertices.txt", "r") as f:
        adj = read_adj_matrix(f, no_e=True, no_v=True, v_sep="x", a_sep="t")
        print_adj_matrix(adj[0], adj[1], adj[2])
        print()
