import igraph as ig


def plot_flownet(graph, layers, weights):
    g = ig.Graph(directed=True)
    g.add_vertices(len(graph))

    for i in range(len(weights)):
        for j in range(0, len(weights)):
            if weights[i][j] is not None:
                g.add_edge(i, j, weight=weights[i][j])

    layout = [(layer, i) for layer in layers for i, _ in enumerate(layers[layer])]

    visual_style = {"vertex_size": 30, "layout": layout, "bbox": (300, 300), "margin": 20, "vertex_label": graph.keys(),
                    "edge_label": g.es['weight'], "vertex_color": 'Dark Olive Green', "edge_width": 2,
                    "background": 'Light Slate Gray'}

    plot = ig.plot(g, **visual_style, return_plot=True)

    return plot
