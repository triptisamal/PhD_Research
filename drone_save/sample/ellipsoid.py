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
number_of_points = 8000
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
h=0
k=0
f=0
u = []

def magnitude(vect):
    return math.sqrt((vect[0])**2+(vect[1])**2+(vect[2])**2)


###METHODS NEEDED FOR ROTATING A POINT

def R():

    global theta
    global u


    return [[round(math.cos(theta),2) + u[0]**2 * (1-round(math.cos(theta),2)), 
             u[0] * u[1] * (1-round(math.cos(theta),2)) - u[2] * round(math.sin(theta),2), 
             u[0] * u[2] * (1 - round(math.cos(theta),2)) + u[1] * round(math.sin(theta),2)],
            [u[0] * u[1] * (1-round(math.cos(theta),2)) + u[2] * round(math.sin(theta),2),
             round(math.cos(theta),2) + u[1]**2 * (1-round(math.cos(theta),2)),
             u[1] * u[2] * (1 - round(math.cos(theta),2)) - u[0] * round(math.sin(theta),2)],
            [u[0] * u[2] * (1-round(math.cos(theta),2)) - u[1] * round(math.sin(theta),2),
             u[1] * u[2] * (1-round(math.cos(theta),2)) + u[0] * round(math.sin(theta),2),
             round(math.cos(theta),2) + u[2]**2 * (1-round(math.cos(theta),2))]]
            
def rotate_point(pointToRotate):
    
    r = R()

    rotated = []
    

  #  for j in range(3):
  #      summ=0
  #      for i in range(3):
  #          #print(pointToRotate[j],"*",r[j][i])
  #          summ += pointToRotate[i]*r[j][i]
  #      rotated.append(round(summ))

    for i in range(3):
        rotated.append(round(sum([r[j][i] * pointToRotate[j] for j in range(3)])))

    return rotated


###METHODS NEEDED FOR ROTATING sd

def R_z(phi,direction):
    
    if direction == 0:#clockwise
        return [[round(math.cos(phi),2),round(math.sin(phi),2),0],
            [-round(math.sin(phi),2),round(math.cos(phi),2),0],
            [0,0,1]]
    if direction == 1:#anticlockwise
        return [[round(math.cos(phi),2),-round(math.sin(phi),2),0],
            [round(math.sin(phi),2),round(math.cos(phi),2),0],
            [0,0,1]]

def R_x(phi,direction):
    
    if direction == 0: #clockwise
        return [[1,0,0],
             [0,round(math.cos(phi),2), round(math.sin(phi),2)],
            [0,-round(math.sin(phi),2),  round(math.cos(phi),2)]]
    if direction == 1: #anticlockwise
        return [[1,0,0],
             [0,round(math.cos(phi),2),-round(math.sin(phi),2)],
            [0,round(math.sin(phi),2),round(math.cos(phi),2)]]
            
            
def rotatez(pointToRotate,phi,direction):

    r = R_z(phi,direction)

    rotated = []

    for j in range(3):
        summ=0
        for i in range(3):
            #print(pointToRotate[i],"*",r[j][i])
            summ += pointToRotate[i]*r[j][i]
        rotated.append(round(summ))

    return rotated

def rotate(pointToRotate,phi,direction):


    r = R_x(phi,direction)

    rotated = []
    

    for j in range(3):
        summ=0
        for i in range(3):
           # print(pointToRotate[i],"*",r[j][i])
            summ += pointToRotate[i]*r[j][i]
        rotated.append(round(summ))


    return rotated


def if_different_zsign(s,d):

    if s[2]>0 and d[2]<0:
        return 1
    elif s[2]<0 and d[2]>0:
        return 1
    else:
        return 0


def find_direction(s):
    ##find direction in which to rotate the vector (anti (1) or clockwise (0))
    
    if s[0]>0 and s[1]>0 and s[2]>0:#+++
        return 0
    elif s[0]<0 and s[1]<0 and s[2]<0:#---
        return 1
    elif s[0]>0 and s[1]<0 and s[2]>0:#+-+
        return 1
    elif s[0]>0 and s[1]>0 and s[2]<0:#++-
        return 0
    elif s[0]>0 and s[1]<0 and s[2]<0:#+--
        return 1
    elif s[0]<0 and s[1]>0 and s[2]<0:#-+-
        return 0
    elif s[0]<0 and s[1]<0 and s[2]>0:#--+
        return 1
    else:#-++
        return 0

def find_angle_between_positionvector_xyplane(vector):

    angle = 0

    iz_vector = [0,0,1]
    angle = math.acos((vector[0]*iz_vector[0]+vector[1]*iz_vector[1]+vector[2]*iz_vector[2])/(magnitude(vector)*magnitude(iz_vector)))
    angle = 1.5708-angle

    return angle


def find_sd_rotated():

    global positions
    global focus1_key
    global focus2_key
    global theta
    global h
    global k
    global f
    s = [positions[focus1_key][0],positions[focus1_key][1],positions[focus1_key][2]]
    d = [positions[focus2_key][0],positions[focus2_key][1],positions[focus2_key][2]]

    #angle between sd_vector and xy plane theta
    iz_vector = [0,0,1]
    iy_vector = [0,1,0]
    ix_vector = [1,0,0]


    #Angle between position vector of s and xy plane
    t1 = find_angle_between_positionvector_xyplane(s)
    direction=find_direction(s)
    
    if(if_different_zsign(s,d)):
        t1=t1+3.14159
    print("Angle between position vector of s and xy plane=",math.degrees(t1))
    _s = rotate(s,t1,direction)
    print("s=",s,"_s=",_s)
    
    #Angle between position vector of d and xy plane
    t2 = find_angle_between_positionvector_xyplane(d)
    direction=find_direction(d)
    print("Angle between position vector of d and xy plane=",math.degrees(t2))
    
    _d = rotate(d,t2,direction)
    print("d=",d,"_d=",_d)

    sd_rotated = [_d[0]-_s[0],_d[1]-_s[1],_d[2]-_s[2]]
    print("sd_rotated (in plane xy)=",sd_rotated)

    #angle between rotated vector and z axis
    theta2 = math.acos((sd_rotated[0]*iz_vector[0]+sd_rotated[1]*iz_vector[1]+sd_rotated[2]*iz_vector[2])/(magnitude(sd_rotated)*magnitude(iz_vector)))
    print("For testing: Angle between rotated vector sd (in xy plane) and z-axis=",math.degrees(theta2))
    
    
    #Angle between position vector of sd_rotated and x axis
    theta1 = math.acos((sd_rotated[0]*ix_vector[0]+sd_rotated[1]*ix_vector[1]+sd_rotated[2]*ix_vector[2])/(magnitude(sd_rotated)*magnitude(ix_vector)))
    print("Angle between position vector of sd_rotated and x axis=",math.degrees(theta1))
    
    
    if (sd_rotated[0]>0 and sd_rotated[1]<0):
        direction=1 #anticlockwise

    if (sd_rotated[0]<0 and sd_rotated[1]>0):
        direction=0 #clockwise
    
    if (sd_rotated[0]>0 and sd_rotated[1]>0):
        direction=0 #clockwise
    
    if (sd_rotated[0]<0 and sd_rotated[1]<0):
        direction=1 #anticlockwise



    __s = rotatez(_s,theta1,direction)
    print("_s=",_s,"__s=",__s)

    __d = rotatez(_d,theta1,direction)
    print("_d=",_d,"__d=",__d)


    finalsd_rotated = [__d[0]-__s[0],__d[1]-__s[1],__d[2]-__s[2]]

    #midpoint

   # h = (__d[0]+__s[0])/2
   # k = (__d[1]+__s[1])/2
   # f = (__d[2]+__s[2])/2
   # print("centre after rotating",h,k,f)

    print("Final sd_vector=",finalsd_rotated)
    
    return finalsd_rotated


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
 
    point = [x,y,z]
    _point = rotate_point(point)
    
    _x = _point[0]
    _y = _point[1]
    _z = _point[2]
    
    centre = [h,k,f]
    _centre = rotate_point(centre)
    _h = _centre[0]
    _k = _centre[1]
    _f = _centre[2]
    

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



def find_theta():

    #theta is the angle sd_rotated and sd 
    global positions
    global focus2_key
    global focus1_key
    global u
    global theta


    sd = [positions[focus2_key][0]-positions[focus1_key][0],positions[focus2_key][1]-positions[focus1_key][1],positions[focus2_key][2]-positions[focus1_key][2]]


    sd_rotated = find_sd_rotated()

    #Axis (vector) perpendicular to both sd and sd_rotated
    v = [sd[1]*sd_rotated[2]+sd[2]*sd_rotated[1],sd[2]*sd_rotated[0]+sd[0]*sd_rotated[2],sd[0]*sd_rotated[1]+sd[1]*sd_rotated[0]]

    #Normalize the cross product to a unit vector u
    u = [v[0]/magnitude(v),v[1]/magnitude(v),v[2]/magnitude(v)]
   # print(u)
    #Dot product between sd and sd_rotated
    theta = math.acos((sd_rotated[0]*sd[0]+sd_rotated[1]*sd[1]+sd_rotated[2]*sd[2])/(magnitude(sd_rotated)*magnitude(sd)))

    print("Angle between final and initial sd=",math.degrees(theta))

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
    global h
    global k
    global f
    print("PETAL PARAMETERS")
    print("----------------")
    
    print("Coordinates of focus 1 (source): (", positions[focus1_key][0],",", positions[focus1_key][1],",", positions[focus1_key][2],")" )
    print("Coordinates of focus 2 (destination): (", positions[focus2_key][0],",", positions[focus2_key][1],",", positions[focus2_key][2],")" )
   

    h = (positions[focus1_key][0]+positions[focus2_key][0])/2
    k = (positions[focus1_key][1]+positions[focus2_key][1])/2
    f = (positions[focus1_key][2]+positions[focus2_key][2])/2

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



    ##Find angle between sd and the sd (rotated) in the equation 
    ##(x-h)**2/(a*a) + (y-k)**2/(b*b) + (z-f)**2/(c*c) <= 1

    find_theta()



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
   
    focus1_key = 23
    focus2_key = 72
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
