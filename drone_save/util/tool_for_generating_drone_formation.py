#find if a point is inside an ellipsoid
import plotly.graph_objects as go
import networkx as nx
from networkx import grid_graph
import random
import math
import pylab
import numpy as np
from shutil import copyfile
from itertools import combinations
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

import sys

number_of_points = 8000
node_loc = []
positions = {}
focus1_key = 0
focus2_key = 0
e=0.8
a=0
b=0
c=0
topology = 0
formation = 0
inputtype = 0
theta = 0
h=0
k=0
f=0


def insideOrNot(location):
    global positions
    global focus1_key
    global focus2_key
    global a
    global b
    global c
    global h
    global k
    global f
    #extract the exact x,y,z coordinates
    x = location[0]
    y = location[1]
    z = location[2]


    v = [positions[focus2_key][0]-positions[focus1_key][0],positions[focus2_key][1]-positions[focus1_key][1],positions[focus2_key][2]-positions[focus1_key][2]]
 
    s = positions[focus2_key][0]-positions[focus1_key][0]
    t = positions[focus2_key][1]-positions[focus1_key][1]
    u = positions[focus2_key][2]-positions[focus1_key][2]
    
    sol = ((t*(f-z)-u*(k-y))**2+(u*(h-x)-s*(f-z))**2+(s*(k-y)-t*(h-x))**2)/((b**2)*(s**2+t**2+u**2)) + ((s*(h-x)+t*(k-y)+u*(f-z))**2)/((a**2)*(s**2+t**2+u**2))


    #print(h,k,f)
    #semi axes are of lengths a, b, c

    if sol <= 1:
       # print(location,sol)
        return 1 #inside
    else:
        if x == positions[focus1_key][0] and y == positions[focus1_key][1] and z == positions[focus1_key][2]:
            print(location,sol)
        if x == positions[focus2_key][0] and y == positions[focus2_key][1] and z == positions[focus2_key][2]:
            print(location,sol)
        return 0



def find_points_inside_ellipsoid():

    global node_loc
    global number_of_points
    global focus1_key 
    global focus2_key 
    ctr = 0
    x = []
    y = []
    z = []
    x1 = []
    y1 = []
    z1 = []
    x2 = []
    y2 = []
    z2 = []
    for i in range(0,number_of_points):
        loc = (node_loc[i]['x'],node_loc[i]['y'],node_loc[i]['z'])
        inside = insideOrNot(loc)
        if inside == 1:
            if i != focus1_key and i != focus2_key:
                x.append(node_loc[i]['x'])
                y.append(node_loc[i]['y'])
                z.append(node_loc[i]['z'])
            #plt.plot(node_loc[i]['x'],node_loc[i]['y'],node_loc[i]['z'], 'o', color='black')
        #    print(i, loc)
            if i == focus1_key or i == focus2_key:
                x2.append(node_loc[i]['x'])
                y2.append(node_loc[i]['y'])
                z2.append(node_loc[i]['z'])
                
            ctr += 1
        else:
            if i == focus1_key or i == focus2_key:
                print("outside: ",i, loc)
            x1.append(node_loc[i]['x'])
            y1.append(node_loc[i]['y'])
            z1.append(node_loc[i]['z'])


    print("Total points inside the ellipsoid: ",ctr)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter(x,y,z, color='blue')
    ax.scatter(x1,y1,z1, color='black')
    ax.scatter(x2,y2,z2, color='red',marker='+')
    plt.show()
    
def initiate_petal_parameters():
    
    
    global positions
    global a
    global b
    global c
    global e
    global focus1_key
    global focus2_key
    global theta
    global h
    global k
    global f
    print("PETAL PARAMETERS")
    print("----------------")
    
    print("Coordinates of focus 1 (source): (", positions[focus1_key][0],",", positions[focus1_key][1],",", positions[focus1_key][2],")" )
    print("Coordinates of focus 2 (destination): (", positions[focus2_key][0],",", positions[focus2_key][1],",", positions[focus2_key][2],")" )
   


    ff = (positions[focus2_key][0]-positions[focus1_key][0])**2 +(positions[focus2_key][1]-positions[focus1_key][1])**2+(positions[focus2_key][2]-positions[focus1_key][2])**2

    focaldist = math.sqrt(ff)
    h = (positions[focus1_key][0]+positions[focus2_key][0])/2
    k = (positions[focus1_key][1]+positions[focus2_key][1])/2
    f = (positions[focus1_key][2]+positions[focus2_key][2])/2
    print("Centre =", h,k,f)
    print("Distance between two foci =", focaldist)
    print("Linear eccentricity =", focaldist/2)
    print("Eccentricity:",e)
    #is that of the ellipse formed by a section containing both the longest and the shortest axes (one of which will be the polar axis (x axis))
    a = focaldist/(2*e)
    print("Semi major axis, a = ", a)

    ma = a+a
    print("major axis, a+a = ", ma)
    c = a * math.sqrt(1-(e)**2)
    print("Semi minor axis, c = ", c)
    print("minor axis, c+c = ", c+c)
    if focaldist > ma:
        print("incorrect")
    #globalvars.c = random.uniform(globalvars.b,globalvars.c)
    # a = b = c: sphere
    # a = b > c: oblate spheroid.
    # a = b < c: prolate spheroid
    # a > b > c: scalene spheroid or triaxial.
    b = c
    print("b = ",b)



    ##(x-h)**2/(a*a) + (y-k)**2/(b*b) + (z-f)**2/(c*c) <= 1




def initiate_source_destination():
   
    global positions
    global focus1_key
    global focus2_key
    global inputtype

    print("SOURCE AND DESTINATION")
    print("------------------------")
    all_position_keys = []

    #print(positions)
    print(inputtype)
    all_position_keys = list(positions.keys())

    
    if inputtype == 3:
        focus1_key = np.random.choice(all_position_keys)
    
        while True:
            focus2_key = np.random.choice(all_position_keys)
            if focus1_key != focus2_key:
                break

    if inputtype == 0:
        if formation == 0:
            copyfile('input_for_cuboid_27000.txt','input.txt')
        f=open('input.txt')
        lines=f.readlines()
        focus1_key = int(lines[0])#23
        focus2_key = int(lines[1])#24
 
    if inputtype == 2:
        if formation == 0:
            copyfile('input_for_cuboid_27000.txt','input.txt')
        if formation == 2:
            copyfile('input_for_hollowsph_3672.txt','input.txt')
        f=open('input.txt')
        lines=f.readlines()
        focus1_key = int(lines[2])#2
        focus2_key = int(lines[3])#26998
    
    if inputtype == 1:
        if formation == 0:
            copyfile('input_for_cuboid_27000.txt','input.txt')
        if formation == 2:
            copyfile('input_for_hollowsph_3672.txt','input.txt')
        f=open('input.txt')
        lines=f.readlines()
        focus1_key = int(lines[4])#24
        focus2_key = int(lines[5])#34
    print("source:",focus1_key)
    print("destination:",focus2_key)

    initiate_petal_parameters()


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



def find_centroid(location):
    x = [p[0] for p in location]
    y = [p[1] for p in location]
    z = [p[2] for p in location]
    centroid = (sum(x) / len(location), sum(y) / len(location), sum(z)/len(location))

    print("centroid",centroid)

    return centroid

def make_sphere(nloc,c,r):
   
    cx=c[0]
    cy=c[1]
    cz=c[2]

    global number_of_points
    global node_loc
    n = 0
    for i in range(0,number_of_points):
        sol = (nloc[i]['x']-cx )**2 + (nloc[i]['y']-cy)**2 + (nloc[i]['z']-cz)**2
        if sol <= r**2:
            node_loc[i]['x'] = nloc[i]['x']
            node_loc[i]['y'] = nloc[i]['y']
            node_loc[i]['z'] = nloc[i]['z']
            n += 1
    
    np = 0
    toremove = []
    for i in range(0,number_of_points):
        if node_loc[i]['x'] == 0 and node_loc[i]['y'] == 0 and node_loc[i]['z'] == 0:
            toremove.append(i)
            np += 1
    
    sorted_toremove = sorted(toremove, reverse=True)
    for index in sorted_toremove:
        del node_loc[index]

    print("number of nodes = ", len(node_loc))
    number_of_points = len(node_loc)
   # print(node_loc)

def make_hollow_sphere(nloc,c,r1,r2):
   
    cx=c[0]
    cy=c[1]
    cz=c[2]

    global number_of_points
    global node_loc
    n = 0
    for i in range(0,number_of_points):
        sol = (nloc[i]['x']-cx )**2 + (nloc[i]['y']-cy)**2 + (nloc[i]['z']-cz)**2
        if sol <= r1**2 and sol > r2**2:
            node_loc[i]['x'] = nloc[i]['x']
            node_loc[i]['y'] = nloc[i]['y']
            node_loc[i]['z'] = nloc[i]['z']
            n += 1
    
    np = 0
    toremove = []
    for i in range(0,number_of_points):
        if node_loc[i]['x'] == 0 and node_loc[i]['y'] == 0 and node_loc[i]['z'] == 0:
            toremove.append(i)
            np += 1
    
    sorted_toremove = sorted(toremove, reverse=True)
    for index in sorted_toremove:
        del node_loc[index]

    print("number of nodes = ", len(node_loc))
    number_of_points = len(node_loc)
   # print(node_loc)




def generate_random_3Dgraph(n_nodes, radius, seed=None):

    global node_loc
    global topology
    global formation
    global number_of_points

    if seed is not None:
        random.seed(seed)
   
    node_loc = [{'x':0, 'y':0, 'z':0} for i in range(0,number_of_points)]

    #wireless range: 25 to 50 feet
    #4 units of distance is 100 feet
    #Total area is 1000 x 1000 x 1000 cubic feet
    


    if formation == 0:
        print("Drone formation is cuboid")
        n = 0
        side = int((number_of_points+1)**(1.0/3))
        #number_of_nodes = 0
        while n < number_of_points:
            for i in range(1,side+1):
                for j in range(1,side+1):
                    for k in range(1,side+1):
                        node_loc[n]['x'] = i
                        node_loc[n]['y'] = j
                        node_loc[n]['z'] = k
                        n += 1
        print("number of nodes = ", len(node_loc))

    if formation == 1:
        print("Drone formation is spherical")
        n = 0
        side = int((number_of_points+1)**(1.0/3))
        nloc = []
        loc = []
        nloc = [{'x':0, 'y':0, 'z':0} for i in range(0,number_of_points+1)]
        #number_of_nodes = 0
        while n < number_of_points:
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
        radius = side/2
        make_sphere(nloc,centre,radius)

    if formation == 2:
        print("Drone formation is hollow spherical")
        n = 0
        side = int((number_of_points+1)**(1.0/3))
        nloc = []
        loc = []
        nloc = [{'x':0, 'y':0, 'z':0} for i in range(0,number_of_points+1)]
        #number_of_nodes = 0
        while n < number_of_points:
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
        radius1 = side/2
        thickness = side/8
        radius2 = radius1 - thickness
        print(radius1)
        print(radius2)
        print(radius1-radius2)
        print(thickness)
        make_hollow_sphere(nloc,centre,radius1,radius2)
    
    n_nodes = number_of_points  
    # Generate a dict of positions
    position = {i: (node_loc[i]['x'], node_loc[i]['y'], node_loc[i]['z']) for i in range(n_nodes)}
    #print(position)
        # Create random 3D network
    G = nx.random_geometric_graph(n_nodes, radius, pos=position)
    
    
    
    
    return G



def network_plot_3D(G, angle,save=False):

    global positions
    # Get node positions
    positions = nx.get_node_attributes(G, 'pos')


   # print("Position of all nodes: ",pos) 
  #  print("Position of all nodes: ",pos.keys()) 
    # Get number of nodes
    n = G.number_of_nodes()


    # 3D network plot
  #  with plt.style.context(('ggplot')):
  #      
  #      fig = plt.figure(figsize=(10,7))
  #      ax = Axes3D(fig)
  #      
  #      # Loop on the pos dictionary to extract the x,y,z coordinates of each node
  #      for key, value in positions.items():
  #          xi = value[0]
  #          yi = value[1]
  #          zi = value[2]
  #          
  #          # Scatter plot
  #          ax.scatter(xi, yi, zi, s=20+20*G.degree(key), edgecolors='k', alpha=0.7)
  #          #ax.scatter(xi, yi, zi, c=colors[key], s=20+20*G.degree(key), edgecolors='k', alpha=0.7)
  #      
  #    #  # Loop on the list of edges to get the x,y,z, coordinates of the connected nodes
  #    #  # Those two points are the extrema of the line to be plotted
  #    #  for i,j in enumerate(G.edges()):

  #    #      x = np.array((positions[j[0]][0], positions[j[1]][0]))
  #    #      y = np.array((positions[j[0]][1], positions[j[1]][1]))
  #    #      z = np.array((positions[j[0]][2], positions[j[1]][2]))
  #    #  
  #    #  # Plot the connecting lines
  #    #      ax.plot(x, y, z, c='black', alpha=0.5)
  #  
  #  # Set the initial view
  #  ax.view_init(30, angle)

  #  # Hide the axes
  #  ax.set_axis_off()

  # #  if save is not False:
  # #      plt.savefig("C:\scratch\\data\"+str(angle).zfill(3)+".png")
  # #      plt.close('all')
  # #  else:
  # #       plt.show()
  #  plt.show()
    
    return


def create_drones_network():

    global number_of_points
    n = number_of_points  
    #n = number_of_nodes  
    G = generate_random_3Dgraph(n_nodes=n, radius=0.25, seed=1)
    network_plot_3D(G,0,save=False)


def main():
    global topology
    global formation
    global inputtype


    if len(sys.argv) < 3:
        print("Usage: tool_for_generating_drone_formation.py <Shape> <Input Type>")
        print("Topology:")
        print("Cuboid: 0")
        print("Spherical: 1")
        print("Howllow spherical: 2")
        print("Input Type:")
        print("S and D next to each other: 0")
        print("S and D next faraway from each other, at the edge: 1")
        print("S and D next faraway from each other, not at the edge (diametrically opposite for hollow sphere): 2")
        print("S and D next random: 3")
    
    formation = int(sys.argv[1])
    inputtype = int(sys.argv[2])

    

    create_drones_network()
    initiate_source_destination()
    find_points_inside_ellipsoid()



if __name__=="__main__":
    main()
