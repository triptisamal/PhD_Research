#find if a point is inside an ellipsoid
import plotly.graph_objects as go
import networkx as nx
from networkx import grid_graph
import random
import math
import pylab
import numpy as np

from itertools import combinations
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

import sys

#number_of_points = 216
number_of_points = 125
node_loc = []
positions = {}
focus1_key = 0
focus2_key = 0
e=0.9
a=0
b=0
c=0
topology = 0
theta = 0
phi = 0
h=0
k=0
f=0
u = []

def magnitude(vect):
    return math.sqrt((vect[0])**2+(vect[1])**2+(vect[2])**2)

def R():

    global theta
    global u
    return [[round(math.cos(theta),2) + u[0]**2 * (1-round(math.cos(theta),2)), 
             u[0] * u[1] * (1-round(math.cos(theta),2)) - u[2] * -round(math.sin(theta),2), 
             u[0] * u[2] * (1 - round(math.cos(theta),2)) + u[1] * -round(math.sin(theta),2)],
            [u[0] * u[1] * (1-round(math.cos(theta),2)) + u[2] * -round(math.sin(theta),2),
             round(math.cos(theta),2) + u[1]**2 * (1-round(math.cos(theta),2)),
             u[1] * u[2] * (1 - round(math.cos(theta),2)) - u[0] * -round(math.sin(theta),2)],
            [u[0] * u[2] * (1-round(math.cos(theta),2)) - u[1] * -round(math.sin(theta),2),
             u[1] * u[2] * (1-round(math.cos(theta),2)) + u[0] * -round(math.sin(theta),2),
             round(math.cos(theta),2) + u[2]**2 * (1-round(math.cos(theta),2))]]

def rotate(pointToRotate, sd_vector, i_vector):
    
    global theta
    global u
    #need to rotate sd_vector by theta in the same plane as both vectors sd_vector and i_vector around an axis perpendicular to the plane
    #cross product of 2 vectors, v gives the vector perpendicular to both vectors
    v = [sd_vector[1]*i_vector[2]+sd_vector[2]*i_vector[1],sd_vector[2]*i_vector[0]+sd_vector[0]*i_vector[2],sd_vector[0]*i_vector[1]+sd_vector[1]*i_vector[0]]

    #Normalize the cross product to a unit vector u

    u = [v[0]/magnitude(v),v[1]/magnitude(v),v[2]/magnitude(v)]

    r = R()

    rotated = []
    

#    for j in range(3):
#        summ=0
#        for i in range(3):
#            #print(pointToRotate[j],"*",r[j][i])
#            summ += pointToRotate[j]*r[j][i]
#        rotated.append(round(summ))

    for i in range(3):
        rotated.append(round(sum([r[j][i] * pointToRotate[j] for j in range(3)])))

    return rotated

def insideOrNot(location):
    global positions
    global focus1_key
    global focus2_key
    global a
    global b
    global c
    global theta
    global h
    global k
    global f
    #extract the exact x,y,z coordinates
    x = location[0]
    y = location[1]
    z = location[2]
 
    sd_vector = [positions[focus2_key][0]-positions[focus1_key][0],positions[focus2_key][1]-positions[focus1_key][1],positions[focus2_key][2]-positions[focus1_key][2]]


    #Find angle of rotation of the point
    #sd_vector needs to be made parallel to x-axis
    i_vector= [1,0,0] #unit vector along x-axis
    #angle made by source-destination line vector with i_vector is theta, found by dot product of the vectors

    theta = math.acos((sd_vector[0]*i_vector[0]+sd_vector[1]*i_vector[1]+sd_vector[2]*i_vector[2])/(magnitude(sd_vector)*magnitude(i_vector)))


   # #new coordinates in rotated ellipse
    point = [x,y,z]
    _point = rotate(point,sd_vector,i_vector)


   # print("projected centre:",_h,_k,_f)  
    _x = _point[0]
    _y = _point[1]
    _z = _point[2]
    sol = (_x-h)**2/(a*a) + (_y-k)**2/(b*b) + (_z-f)**2/(c*c)
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
    for i in range(0,number_of_points):
        loc = (node_loc[i]['x'],node_loc[i]['y'],node_loc[i]['z'])
        inside = insideOrNot(loc)
        if inside == 1:
            x.append(node_loc[i]['x'])
            y.append(node_loc[i]['y'])
            z.append(node_loc[i]['z'])
            #plt.plot(node_loc[i]['x'],node_loc[i]['y'],node_loc[i]['z'], 'o', color='black')
        #    print(i, loc)
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
    ax.scatter(x,y,z, color='red')
    ax.scatter(x1,y1,z1, color='black')
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
    global phi
    global h
    global k
    global f
    print("PETAL PARAMETERS")
    print("----------------")
    
    print("Coordinates of focus 1 (source): (", positions[focus1_key][0],",", positions[focus1_key][1],",", positions[focus1_key][2],")" )
    print("Coordinates of focus 2 (destination): (", positions[focus2_key][0],",", positions[focus2_key][1],",", positions[focus2_key][2],")" )
   
    
    sd_vector = [positions[focus2_key][0]-positions[focus1_key][0],positions[focus2_key][1]-positions[focus1_key][1],positions[focus2_key][2]-positions[focus1_key][2]]


    #Find angle of rotation of the point
    #sd_vector needs to be made parallel to x-axis
    i_vector= [1,0,0] #unit vector along x-axis
    #angle made by source-destination line vector with i_vector is theta, found by dot product of the vectors

    theta = math.acos((sd_vector[0]*i_vector[0]+sd_vector[1]*i_vector[1]+sd_vector[2]*i_vector[2])/(magnitude(sd_vector)*magnitude(i_vector)))


#   # #new coordinates in rotated ellipse
#    point_f2 = [positions[focus2_key][0],positions[focus2_key][1],positions[focus2_key][2]]
#    _point_f2 = rotate(point_f2,sd_vector,i_vector)
#    point_f1 = [positions[focus1_key][0],positions[focus1_key][1],positions[focus1_key][2]]
#    _point_f1 = rotate(point_f1,sd_vector,i_vector)
#    
#
#    h = (_point_f2[0]+_point_f1[0])/2
#    k = (_point_f2[1]+_point_f1[1])/2
#    f = (_point_f2[2]+_point_f1[2])/2
#    
#    
#    
#    h = (positions[focus1_key][0]+positions[focus2_key][0])/2
#    k = (positions[focus1_key][1]+positions[focus2_key][1])/2
#    f = (positions[focus1_key][2]+positions[focus2_key][2])/2



#    ff = (_point_f2[0]-_point_f1[0])**2 +(_point_f2[1]-_point_f1[1])**2+(_point_f2[2]-_point_f1[2])**2
    ff = (positions[focus2_key][0]-positions[focus1_key][0])**2 +(positions[focus2_key][1]-positions[focus1_key][1])**2+(positions[focus2_key][2]-positions[focus1_key][2])**2

    focaldist = math.sqrt(ff)
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
    #b = random.uniform(a,c) #[a,c)
    print("b = ",b)

def initiate_source_destination():
   
    global positions
    global focus1_key
    global focus2_key

    print("SOURCE AND DESTINATION")
    print("------------------------")
    all_position_keys = []

    #print(positions)
    all_position_keys = list(positions.keys())
    focus1_key = np.random.choice(all_position_keys)
    
    while True:
        focus2_key = np.random.choice(all_position_keys)
        if focus1_key != focus2_key:
            break
   
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


def generate_random_3Dgraph(n_nodes, radius, seed=None):

    global node_loc
    global topology

    if seed is not None:
        random.seed(seed)
   
    node_loc = [{'x':0, 'y':0, 'z':0} for i in range(0,number_of_points+1)]

    #wireless range: 25 to 50 feet
    #4 units of distance is 100 feet
    #Total area is 1000 x 1000 x 1000 cubic feet
    


   # if topology == 0:
    print("topology is cuboid")
    n = 0
    side = int((number_of_points+1)**(1.0/3))
    n=0
    number_of_nodes = 0
    while n < number_of_points:
        for i in range(1,side+1):
            for j in range(1,side+1):
                for k in range(1,side+1):
                    node_loc[n]['x'] = i
                    node_loc[n]['y'] = j
                    node_loc[n]['z'] = k
                    n += 1
    # Generate a dict of positions
    position = {i: (node_loc[i]['x'], node_loc[i]['y'], node_loc[i]['z']) for i in range(n_nodes)}
    print(position)
        # Create random 3D network
    G = nx.random_geometric_graph(n_nodes, radius, pos=position)
    
    
    
    
    return G



def network_plot_3D(G, angle,save=False):

    global positions
    # Get node positions
    positions = nx.get_node_attributes(G, 'pos')


#   # print("Position of all nodes: ",pos) 
#  #  print("Position of all nodes: ",pos.keys()) 
#    # Get number of nodes
#    n = G.number_of_nodes()
#
#
#    # 3D network plot
#    with plt.style.context(('ggplot')):
#        
#        fig = plt.figure(figsize=(10,7))
#        ax = Axes3D(fig)
#        
#        # Loop on the pos dictionary to extract the x,y,z coordinates of each node
#        for key, value in positions.items():
#            xi = value[0]
#            yi = value[1]
#            zi = value[2]
#            
#            # Scatter plot
#            ax.scatter(xi, yi, zi, s=20+20*G.degree(key), edgecolors='k', alpha=0.7)
#            #ax.scatter(xi, yi, zi, c=colors[key], s=20+20*G.degree(key), edgecolors='k', alpha=0.7)
#        
#        # Loop on the list of edges to get the x,y,z, coordinates of the connected nodes
#        # Those two points are the extrema of the line to be plotted
#        for i,j in enumerate(G.edges()):
#
#            x = np.array((positions[j[0]][0], positions[j[1]][0]))
#            y = np.array((positions[j[0]][1], positions[j[1]][1]))
#            z = np.array((positions[j[0]][2], positions[j[1]][2]))
#        
#        # Plot the connecting lines
#            ax.plot(x, y, z, c='black', alpha=0.5)
#    
#    # Set the initial view
#    ax.view_init(30, angle)
#
#    # Hide the axes
#    ax.set_axis_off()
#
#   #  if save is not False:
#   #      plt.savefig("C:\scratch\\data\"+str(angle).zfill(3)+".png")
#   #      plt.close('all')
#   #  else:
#   #       plt.show()
#   # plt.show()
#    
    return


def create_drones_network():

    n = number_of_points  
    #n = number_of_nodes  
    G = generate_random_3Dgraph(n_nodes=n, radius=0.25, seed=1)
    network_plot_3D(G,0,save=False)


def main():
    global topology


    if len(sys.argv) < 2:
        print("Usage: latticeovoid.py <topology>")
    
    topology = sys.argv[1]

    create_drones_network()
    initiate_source_destination()
    find_points_inside_ellipsoid()



if __name__=="__main__":
    main()
