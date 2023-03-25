import igraph as ig
import matplotlib.pyplot as plt

g = {0: [1, 2, 3, 4], 1: [0, 2, 3, 4],
     2: [0, 1, 3, 6], 3: [0, 1, 2, 4], 4: [0, 1, 3, 5], 5: [4, 6], 6: [2, 5]}  # przyklad z zajec
g_plot = ig.Graph.ListDict(g)
fig, ax = plt.subplots(figsize=(5, 5))

ig.plot(
    g_plot,
    target=ax,
    layout="circle",
    vertex_size=0.3,
    vertex_frame_width=8.0,
    vertex_frame_color="white",
    vertex_label=g.keys(),
    vertex_label_size=7.0
)

ig.plot(g_plot)
plt.show()
