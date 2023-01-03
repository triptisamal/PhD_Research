import globalvars


#import plotly.graph_objects as go
import networkx as nx
import random
import numpy as np
from itertools import combinations
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import math

def generate_adjlist_with_all_edges(G,delimiter):
    for s, nbrs in G.adjacency():
        line = str(s) + delimiter
        for t, data in nbrs.items():
            line += str(t) + delimiter
        yield line[: -len(delimiter)]

def find_centroid(received_from_location):
    x = [p[0] for p in received_from_location]
    y = [p[1] for p in received_from_location]
    z = [p[2] for p in received_from_location]
    centroid = (sum(x) / len(received_from_location), sum(y) / len(received_from_location), sum(z)/len(received_from_location))

    print("centroid",centroid)

    return centroid

def distance_between_nodes(u, v, node_loc):
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
   
    node_loc = [{'x':0, 'y':0, 'z':0} for i in range(0,globalvars.number_of_nodes+1)]

    #wireless range: 25 to 50 feet
    #4 units of distance is 100 feet
    #Total area is 1000 x 1000 x 1000 cubic feet


    if globalvars.formation == 0: #cuboid
        print("Drone formation is cuboid")
        if globalvars.topology == 0: #Perfect Lattice
            print("Drone topology is perfect lattice")
            n = 0
            side = int((globalvars.number_of_nodes+1)**(1.0/3))
            print(globalvars.number_of_nodes)
            print(side)
            while n < globalvars.number_of_nodes:
                for i in range(1,side+1):
                    for j in range(1,side+1):
                        for k in range(1,side+1):
                            node_loc[n]['x'] = i
                            node_loc[n]['y'] = j
                            node_loc[n]['z'] = k
                            n += 1

        if globalvars.topology == 1: #Gaussian Perturbation Lattice
            n = 0
            side = int((globalvars.number_of_nodes+1)**(1.0/3))
            print(globalvars.number_of_nodes)
            print(side)

            #gaussian noise
            mu = 0
            sigma = 0.2
            noise = np.random.normal(mu, sigma, [globalvars.number_of_nodes])
            while n < globalvars.number_of_nodes:
                for i in range(1,side+1):
                    for j in range(1,side+1):
                        for k in range(1,side+1):
                            node_loc[n]['x'] = i + noise[n]
                            node_loc[n]['y'] = j + noise[n]
                            node_loc[n]['z'] = k + noise[n]
                        n += 1


    if globalvars.formation == 2:
        print("Drone formation is hollow spherical")
        n = 0
        side = int((globalvars.number_of_nodes+1)**(1.0/3))
        nloc = []
        loc = []
        nloc = [{'x':0, 'y':0, 'z':0} for i in range(0,globalvars.number_of_nodes+1)]
        #number_of_nodes = 0
        while n < globalvars.number_of_nodes:
            for i in range(1,side+1):
                for j in range(1,side+1):
                    for k in range(1,side+1):
                        nloc[n]['x'] = i
                        nloc[n]['y'] = j
                        nloc[n]['z'] = k
                        tup = (i,j,k)
                        loc.append(tup)
                        n += 1

        centre = find_centroid(loc)
        #radius1 = side/2
        r1 = side/2
        thickness = side/8
        #radius2 = radius1 - thickness
        r2 = r1 - thickness
        #print(radius1)
        #print(radius2)
        #print(radius1-radius2)
        #print(thickness)
        #make_hollow_sphere(nloc,centre,radius1,radius2)



        cx=centre[0]
        cy=centre[1]
        cz=centre[2]

        n = 0
        for i in range(0,globalvars.number_of_nodes):
            sol = (nloc[i]['x']-cx )**2 + (nloc[i]['y']-cy)**2 + (nloc[i]['z']-cz)**2
            if sol <= r1**2 and sol > r2**2:
                node_loc[i]['x'] = nloc[i]['x']
                node_loc[i]['y'] = nloc[i]['y']
                node_loc[i]['z'] = nloc[i]['z']
                n += 1
        
        np = 0
        toremove = []
        for i in range(0,globalvars.number_of_nodes):
            if node_loc[i]['x'] == 0 and node_loc[i]['y'] == 0 and node_loc[i]['z'] == 0:
                toremove.append(i)
                np += 1
        
        sorted_toremove = sorted(toremove, reverse=True)
        for index in sorted_toremove:
            del node_loc[index]

        print("number of nodes = ", len(node_loc))
        globalvars.number_of_nodes = len(node_loc)

    n_nodes = globalvars.number_of_nodes

    # Generate a dict of positions
    position = {i: (node_loc[i]['x'], node_loc[i]['y'], node_loc[i]['z']) for i in range(n_nodes)}
    print("Generating a dict of positions")
    # Create random 3D network

    globalvars.G = nx.random_geometric_graph(n_nodes, radius, pos=position)
    print("G is populated")
    
    
    globalvars.pos = nx.get_node_attributes(globalvars.G, 'pos')
    print("Position of all nodes initially: ",globalvars.pos) 



    #if globalvars.sd_random == 1:
    to_del = []
    for u, v in combinations(globalvars.G, 2):
      dist = distance_between_nodes(u,v,node_loc)
      #print(dist)
      if dist <= 0.4: #if distance is less than 10 feet
          print("distance=",dist," : nodes are too close, removing")
          to_del.append(u)
          to_del.append(v)
          continue
      if dist >= 2: #if distance is more than 50 feet
          pass
      elif dist < 1: #if distance is less than 25 feet
          globalvars.G.add_edge(u, v)
      else:
          p = 1 - ((dist - 1)/1)
          q = random.uniform(0,1)
          if q <= p:
              globalvars.G.add_edge(u, v)
    globalvars.G.remove_nodes_from(to_del)

    print("removed nodes = ",to_del)
    print("NUMBER OF NODES = ",len(globalvars.G.nodes))
    globalvars.number_of_nodes = globalvars.G.number_of_nodes()

    #write to file
    original_stdout = sys.stdout
    with open('./files/postionstart.txt','w') as fp:
        sys.stdout = fp
        for line in generate_adjlist_with_all_edges(globalvars.G,' '):
            print(line)

    sys.stdout = original_stdout
    fp.close()

    #for line in generate_adjlist_with_all_edges(globalvars.G,' '):
    #    print(line)
    #save_adj_list_in_file()

   # else:
     #   #Read Adjacency matrix from file
    #    read_adj_list_from_file()
        

    return globalvars.G


def network_plot_3D(G, angle, save=False):

    # Get node positions
    globalvars.pos = nx.get_node_attributes(G, 'pos')
    print("Position of all nodes: ",globalvars.pos) 
    # Get number of nodes
    n = G.number_of_nodes()
    # Get the maximum number of edges adjacent to a single node
    #edge_max = max([G.degree(i) for i in range(n)])

    # Define color range proportional to number of edges adjacent to a single node
 #   colors = [plt.cm.plasma(G.degree(i)/edge_max) for i in range(n)] 

    # 3D network plot
    with plt.style.context(('ggplot')):
        
        fig = plt.figure(figsize=(10,7))
        ax = Axes3D(fig)
        
        # Loop on the pos dictionary to extract the x,y,z coordinates of each node
        for key, value in globalvars.pos.items():
            xi = value[0]
            yi = value[1]
            zi = value[2]
            
            # Scatter plot
            ax.scatter(xi, yi, zi, s=20+20*G.degree(key), edgecolors='k', alpha=0.7)
            #ax.scatter(xi, yi, zi, c=colors[key], s=20+20*G.degree(key), edgecolors='k', alpha=0.7)
        
        # Loop on the list of edges to get the x,y,z, coordinates of the connected nodes
        # Those two points are the extrema of the line to be plotted
        for i,j in enumerate(G.edges()):

            x = np.array((globalvars.pos[j[0]][0], globalvars.pos[j[1]][0]))
            y = np.array((globalvars.pos[j[0]][1], globalvars.pos[j[1]][1]))
            z = np.array((globalvars.pos[j[0]][2], globalvars.pos[j[1]][2]))
        
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
  #  plt.show()
    
    return


def create_drones_startpos():
    n = globalvars.number_of_nodes  
    G = generate_random_3Dgraph(n_nodes=n, radius=0.25, seed=1)
    network_plot_3D(G,0, save=False)
    
    
    x_nodes = [globalvars.pos[key][-1] for key in globalvars.pos.keys()]
    y_nodes = [globalvars.pos[key][0] for key in globalvars.pos.keys()]
    z_nodes = [globalvars.pos[key][1] for key in globalvars.pos.keys()]
    
    #assign node id to each coordinate
    globalvars.node = [{'nodeID':-1, 'loc':(0,0,0), 'packet':0} for i in range(globalvars.number_of_nodes)]
    for i in range(globalvars.number_of_nodes):
        globalvars.node[i]['nodeID'] = i
        globalvars.node[i]['loc'] = (x_nodes[i],y_nodes[i],z_nodes[i])
        globalvars.node[i]['packet'] = -1
    #print("NODES")
    #print("----------------")
    #print(globalvars.node)

   
    #update number of nodes
    globalvars.number_of_nodes = len(globalvars.G.nodes())
    #make adj list correct (both directions) 
#    print("ADJACENCY LIST")
#    print("----------------")

  #  for line in generate_adjlist_with_all_edges(globalvars.G,' '):
  #      print(line)



