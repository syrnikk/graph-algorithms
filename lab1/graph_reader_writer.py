import csv
import numpy as np


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

        if h[1] != '':
            values = list(map(lambda x: int(x), [h[1], *d[1:]]))
            result.append((int(h[0]), values))
        else:
            result.append((int(h[0]), []))

    return dict(result)


def read_incidence_matrix(src, no_v=False, no_e=False, v_sep=" ", e_sep=" ", a_sep=","):
    """Function that reads graph represented as incidence matrix

    Args:
        src (string): string value of graph represented as incidence matrix
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
            matrix.append([h[1], *d[1:]])
        else:
            matrix.append(d)

    matrix = np.matrix(matrix, dtype=int)

    if (len(edges) != matrix.shape[1] and not no_e) or (matrix > 1).any():
        raise ValueError('Incorrect matrix')

    return (vertices, edges, matrix)


def read_nei_matrix(src, v=False, v_sep=" ", n_sep=","):
    """Function that reads graph represented as neighbor matrix

    Args:
        src (string): string value of graph represented as neighbor matrix 
        v (bool, optional): vertices labels. Defaults to False.
        v_sep (str, optional): vertices separator. Defaults to " ".
        n_sep (str, optional): neighbors separator. Defaults to ",".

    Returns:
        tuple: tuple containing (vertices, matrix)
    """

    data = list(map(lambda x: x[:-1], src))
    vertices = [i+1 for i in range(len(data))] if not v else []
    matrix = list(map(lambda x: x.split(n_sep), data))

    for i, r in enumerate(matrix):
        if v:
            first_cell = r[0].split(v_sep)
            vertices.append(first_cell[0])
            matrix[i][0] = first_cell[1]

    if len(vertices) != len(matrix[0]):
        raise ValueError('Incorrect matrix shape')

    matrix = np.matrix(matrix, dtype=int)

    if (matrix > 1).any():
        raise ValueError('Incorrect matrix')

    return (vertices, matrix)


def print_list(list):
    """Function printing the graph from the list form

    Args:
        list (dictionary): list representation of the graph
    """

    for k, v in list.items():
        print(k, end=": ")
        print(",".join(map(lambda x: str(x), v)))


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

    shape = np.shape(matrix)

    if len(vertices) != shape[0]:
        raise ValueError("Lengths do not match")
    print(sep.join([str(i) for i in vertices]))

    if display_dashes:
        print(sep.join(["-" for _ in range(len(vertices))]))

    for i in range(shape[0]):
        for j in range(shape[1]):
            print(matrix[i, j], end=sep)
        print()


def print_incidence_matrix(vertices, edges, matrix, sep=" "):
    """Function printing the graph from the adjacency matrix form

    Args:
        vertices (list): list of vertices
        edges (list): list of edges
        matrix (2d-list): adjacency matrix
        sep (str, optional): printing separator. Defaults to " ".
    """

    shape = np.shape(matrix)

    print(f'{sep}{sep.join([str(e) for e in edges])}')

    for i in range(shape[0]):
        if len(vertices) > 0:
            print(vertices[i], end=sep)
        for j in range(shape[1]):
            print(matrix[i, j], end=sep)
        print()


if __name__ == "__main__":
    with open("./examples/list.txt", "r") as f:
        li = read_list(f, v_sep=";", n_sep=",")
        print_list(li)
        print()
    with open("./examples/list_2.txt", "r") as f:
        li = read_list(f, v_sep="-", n_sep="n")
        print_list(li)
        print()
    with open("./examples/nei_matrix.txt", "r") as f:
        mt = read_nei_matrix(f, v=False, v_sep=" ", n_sep=" ")
        print_nei_matrix(mt[0], mt[1])
        print()
    with open("./examples/nei_matrix_2.txt", "r") as f:
        mt = read_nei_matrix(f, v=True, v_sep="t", n_sep=" ")
        print_nei_matrix(mt[0], mt[1])
        print()
    try:
        with open("./examples/nei_matrix_3.txt", "r") as f:
            mt = read_nei_matrix(f, v=False, n_sep="u")
            print_nei_matrix(mt[0], mt[1])
            print()
    except ValueError as e:
        print(e)
    try:
        with open("./examples/nei_matrix_4.txt", "r") as f:
            mt = read_nei_matrix(f, v=False, n_sep="k")
            print_nei_matrix(mt[0], mt[1])
            print()
    except ValueError as e:
        print(e)
    with open("./examples/inc_matrix.txt", "r") as f:
        adj = read_incidence_matrix(f, v_sep=";", e_sep="f", a_sep=" ")
        print_incidence_matrix(adj[0], adj[1], adj[2])
        print()
    with open("./examples/inc_matrix_no_header.txt", "r") as f:
        adj = read_incidence_matrix(f, no_e=True, v_sep="x", a_sep=" ")
        print_incidence_matrix(adj[0], adj[1], adj[2])
        print()
    try:
        with open("./examples/inc_matrix_no_header_2.txt", "r") as f:
            adj = read_incidence_matrix(f, no_e=True, v_sep="x", a_sep=".")
            print_incidence_matrix(adj[0], adj[1], adj[2])
            print()
    except ValueError as e:
        print(e)
    with open("./examples/inc_matrix_no_header_3.txt", "r") as f:
        adj = read_incidence_matrix(f, no_e=True, v_sep="q", a_sep=".")
        print_incidence_matrix(adj[0], adj[1], adj[2])
        print()
    try:
        with open("./examples/inc_matrix_2.txt", "r") as f:
            adj = read_incidence_matrix(f, v_sep=";", e_sep="f", a_sep=" ")
            print_incidence_matrix(adj[0], adj[1], adj[2])
            print()
    except ValueError as e:
        print(e)
