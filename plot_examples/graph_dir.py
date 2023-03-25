import igraph
from matplotlib import pyplot as plt

fig, ax = plt.subplots(figsize=(5, 5))
# Dictionary representation of graph with weights
graph_dict = {'A': {'B': 1, 'C': 2}, 'B': {'C': 3}, 'C': {'A': 4}}

# Create graph object
g = igraph.Graph(directed=True)

# Add vertices
g.add_vertices(list(graph_dict.keys()))

# Add edges with weights
for vertex, edges in graph_dict.items():
    for edge, weight in edges.items():
        g.add_edge(vertex, edge, weight=weight)

# Plot graph
igraph.plot(g, target=ax, vertex_label=g.vs['name'], edge_label=g.es['weight'])

plt.show()
