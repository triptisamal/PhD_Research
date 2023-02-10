import random
import networkx as nx
n = 20

pos = {i: (random.gauss(0, 2), random.gauss(0, 2)) for i in range(n)}

G = nx.random_geometric_graph(n, 0.2, pos=pos)
print(G.edges())
