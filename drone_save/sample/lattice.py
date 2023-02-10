import networkx as nx
import matplotlib.pyplot as plt

G = nx.grid_graph(dim=(3,4,5))
#plt.subplot(111)
#node_pos=nx.get_node_attributes(G,'pos')
#
#print(node_pos)
edges = list(G.edges())
#print(edges)

nodes = G.nodes()
print(nodes)



G.remove_edges_from(edges)
#G1 = nx.create_empty_copy(G,with_data=True)
nodes = G.nodes()
print(nodes)
nx.draw(G, with_labels=True, font_weight='bold')
#nx.draw(G1, with_labels=True, font_weight='bold')
plt.show()
