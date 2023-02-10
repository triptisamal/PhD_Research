#https://www.idtools.com.au/3d-network-graphs-with-python-and-the-mplot3d-toolkit/

import random, math
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import pylab
from itertools import combinations

# Calc distance given (x1,x2,y1,y2)
#def distance(x1,x2,y1,y2,z1,z2):
#    return math.sqrt(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))
def distance(u, v, node_loc):
    x1 = node_loc[u]['x']
    x2 = node_loc[v]['x']
    y1 = node_loc[u]['y']
    y2 = node_loc[v]['y']
    z1 = node_loc[u]['z']
    z2 = node_loc[v]['z']
    
    dd = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2-z1)*(z2-z1)
    d = math.sqrt(dd)
    return d

# Generate coordinate value
def coord_val():
    # node needs x and y coordinates (floats) from 0->100
    return random.uniform(0.0,1.0)

def main():
    # The distance that applies to link generation
    d = 20

    # Make a graph and name it
    g = nx.Graph(dim=3,name = "10x10x5 Field Random Network")

    node_loc = [{'x':coord_val(), 'y':coord_val(), 'z':coord_val()} for i in range(500)]
    
    n = 0
    while n < 500:
        for i in range(10):
            for j in range(5):
                for k in range(10):
                    node_loc[n]['x'] = i
                    node_loc[n]['y'] = j
                    node_loc[n]['z'] = k
                    n += 1
    
    
    
    for num in range(0,500):
        print(node_loc[num]['x'],node_loc[num]['y'],node_loc[num]['z'])

    for num in range(0,500):
        g.add_node(num,pos=(node_loc[num]['x'],node_loc[num]['y'],node_loc[num]['z']))
   # pos = nx.spring_layout(g)
    pos=nx.get_node_attributes(g,'pos')
    print(pos)
    for n in range(499):
        for rl in range(499):
            # Check the distance, if < d, generate edge
            if distance(n, rl, node_loc) < d:
                # add edge
                g.add_edge(n,rl)
    to_del = []
    for u, v in combinations(g, 2):
      dist = distance(u,v,node_loc)
      if dist <= 0.001:
          print("distance=",dist," : nodes are too close, removing")
          to_del.append(u)
          to_del.append(v)
          continue
      if dist >= 0.25:
          pass
      elif dist < 0.09:
          g.add_edge(u, v)
      else:
          p = 1 - ((dist - 0.09)/0.16)
          q = random.uniform(0,1)
          if q <= p:
              g.add_edge(u, v)
    g.remove_nodes_from(to_del)
   
   # plot
    pylab.figure(1,figsize=(10,10))
    options = {
    "node_color": "blue",
    "node_size": 30,
    "edge_color": "grey",
    "linewidths": 0,
    "width": 0.6,
    }
   # nx.draw(g, pos, cmap = plt.get_cmap('ocean'),**options)
    nx.draw_networkx_edges(g, pos)
    plt.show()

if __name__ == '__main__':
    main()

#import networkx as nx
#import matplotlib.pyplot as plt
#import pylab 
#
#G = nx.grid_graph(dim=[4,4,4])
#pos = nx.spring_layout(G,dim=3)
#print(pos)
#
##plot the figure
#pylab.figure(1,figsize=(10,10))
#options = {
#"node_color": "blue",
#"node_size": 30,
#"edge_color": "grey",
#"linewidths": 0,
#"width": 0.6,
#}
#
#nx.draw(G, cmap = plt.get_cmap('ocean'),**options)
#plt.show()
