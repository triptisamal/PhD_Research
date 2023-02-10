import random
import networkx as nx
from itertools import combinations
import matplotlib.pyplot as plt
import math

def distance(u, v):
    x1 = pos[u][0]
    x2 = pos[v][0]
    y1 = pos[u][1]
    y2 = pos[v][1]
    z1 = pos[u][2]
    z2 = pos[v][2]
    
    dd = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2-z1)*(z2-z1)
    d = math.sqrt(dd)
    return d
# probability for an edge to exist
#p = 0.3

n=30
m=0
g = nx.gnm_random_graph(n, m)

seed = 20169
pos = nx.random_layout(g,seed=seed,dim=3,center=(0,0,0))  # Seed for reproducible layout
#pos = nx.spring_layout(g,seed=seed,dim=3,scale=10) 

x_nodes = [pos[key][0] for key in pos.keys()]
y_nodes = [pos[key][1] for key in pos.keys()]
z_nodes = [pos[key][2] for key in pos.keys()]
print(x_nodes)
for u, v in combinations(g, 2):
    dist=distance(u,v)
    if dist >= 0.5:# 35 feet
        pass
    elif dist < 0.3:
        g.add_edge(u, v)
    else:
        p = 1 - ((dist - 0.3)/0.2)
        q = random.uniform(0,1)
        if q <= p:
            g.add_edge(u, v)

nx.draw(g, cmap = plt.get_cmap('jet'))
plt.show()


