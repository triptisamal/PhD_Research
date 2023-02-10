"""
===========
Erdos Renyi
===========

Create an G{n,m} random graph with n nodes and m edges
and report some properties.

This graph is sometimes called the Erdős-Rényi graph
but is different from G{n,p} or binomial_graph which is also
sometimes called the Erdős-Rényi graph.
"""

#import matplotlib.pyplot as plt
import plotly.graph_objects as go
import networkx as nx

n = 30  # 10 nodes
m = 50  # 20 edges
#seed = 20160  # seed random number generators for reproducibility

# Use seed for reproducibility
#G = nx.gnm_random_graph(n, m, seed=seed)
G = nx.gnm_random_graph(n, m)
edges = G.edges()
# some properties
print("node degree clustering")
for v in nx.nodes(G):
    print(f"{v} {nx.degree(G, v)} ")

print()
print("the adjacency list")
for line in nx.generate_adjlist(G):
    print(line)

#pos = nx.spring_layout(G, seed=seed,dim=3)  # Seed for reproducible layout
pos = nx.spring_layout(G,dim=3)  # Seed for reproducible layout


x_nodes = [pos[key][0] for key in pos.keys()]
y_nodes = [pos[key][1] for key in pos.keys()]
z_nodes = [pos[key][2] for key in pos.keys()]


#we need to create lists that contain the starting and ending coordinates of each edge.
x_edges=[]
y_edges=[]
z_edges=[]

#need to fill these with all of the coordinates
for edge in edges:
    #format: [beginning,ending,None]
    x_coords = [pos[edge[0]][0],pos[edge[1]][0],None]
    x_edges += x_coords

    y_coords = [pos[edge[0]][1],pos[edge[1]][1],None]
    y_edges += y_coords

    z_coords = [pos[edge[0]][2],pos[edge[1]][2],None]
    z_edges += z_coords



#create a trace for the edges
trace_edges = go.Scatter3d(
    x=x_edges,
    y=y_edges,
    z=z_edges,
    mode='lines',
    line=dict(color='black', width=2),
    hoverinfo='none')

#create a trace for the nodes
trace_nodes = go.Scatter3d(
    x=x_nodes,
    y=y_nodes,
    z=z_nodes,
    mode='markers',
    marker=dict(symbol='circle',
            size=10,
            color='skyblue')
    )

#Include the traces we want to plot and create a figure
data = [trace_edges, trace_nodes]
fig = go.Figure(data=data)

fig.show()



#positions = { node: (int(p[0]),int(p[1])) for node,p in pos.items() }
#print(positions)


#nx.draw(G, pos=pos)
#plt.show()
