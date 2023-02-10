import networkx as nx

import matplotlib.pyplot as plt

G = nx.path_graph(10)

shells = [[0], [1, 2, 3, 4, 5, 6, 7, 8, 9]]

pos = nx.shell_layout(G, shells)
nx.draw_networkx(G, pos)
print(pos)
plt.show()
