import networkx as nx
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import combinations


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

def generate_random_3Dgraph(n_nodes, radius, seed=None):

    if seed is not None:
        random.seed(seed)
   
    node_loc = [{'x':0, 'y':0, 'z':0} for i in range(125)]
    n = 0
    while n < 125:
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    node_loc[n]['x'] = i
                    node_loc[n]['y'] = j
                    node_loc[n]['z'] = k
                    n += 1

    # Generate a dict of positions
    #pos = {i: (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)) for i in range(n_nodes)}
    pos = {i: (node_loc[i]['x'], node_loc[i]['y'], node_loc[i]['z']) for i in range(n_nodes)}
    
    # Create random 3D network
    G = nx.random_geometric_graph(n_nodes, radius, pos=pos)



    #wireless range: 25 to 50 feet
    #4 units of distance is 100 feet

    to_del = []
    for u, v in combinations(G, 2):
      dist = distance(u,v,node_loc)
      #print(dist)
      if dist <= 0.4:
          print("distance=",dist," : nodes are too close, removing")
          to_del.append(u)
          to_del.append(v)
          continue
      if dist >= 2:
          pass
      elif dist < 1:
          G.add_edge(u, v)
      else:
          p = 1 - ((dist - 1)/1)
          q = random.uniform(0,1)
          if q <= p:
              G.add_edge(u, v)
    G.remove_nodes_from(to_del)

    return G



def network_plot_3D(G, angle, save=False):

    # Get node positions
    pos = nx.get_node_attributes(G, 'pos')
    
    # Get number of nodes
    n = G.number_of_nodes()

    # Get the maximum number of edges adjacent to a single node
    edge_max = max([G.degree(i) for i in range(n)])

    # Define color range proportional to number of edges adjacent to a single node
 #   colors = [plt.cm.plasma(G.degree(i)/edge_max) for i in range(n)] 

    # 3D network plot
    with plt.style.context(('ggplot')):
        
        fig = plt.figure(figsize=(10,7))
        ax = Axes3D(fig)
        
        # Loop on the pos dictionary to extract the x,y,z coordinates of each node
        for key, value in pos.items():
            xi = value[0]
            yi = value[1]
            zi = value[2]
            
            # Scatter plot
            ax.scatter(xi, yi, zi, s=20+20*G.degree(key), edgecolors='k', alpha=0.7)
            #ax.scatter(xi, yi, zi, c=colors[key], s=20+20*G.degree(key), edgecolors='k', alpha=0.7)
        
        # Loop on the list of edges to get the x,y,z, coordinates of the connected nodes
        # Those two points are the extrema of the line to be plotted
        for i,j in enumerate(G.edges()):

            x = np.array((pos[j[0]][0], pos[j[1]][0]))
            y = np.array((pos[j[0]][1], pos[j[1]][1]))
            z = np.array((pos[j[0]][2], pos[j[1]][2]))
        
        # Plot the connecting lines
            ax.plot(x, y, z, c='black', alpha=0.5)
    
    # Set the initial view
    ax.view_init(30, angle)

    # Hide the axes
    ax.set_axis_off()

   #  if save is not False:
   #      plt.savefig("C:\scratch\\data\"+str(angle).zfill(3)+".png")
   #      plt.close('all')
   #  else:
   #       plt.show()
    plt.show()
    
    return



n=125
G = generate_random_3Dgraph(n_nodes=n, radius=0.25, seed=1)
network_plot_3D(G,0, save=False)
