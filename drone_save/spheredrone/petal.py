#find if a point is inside an ellipsoid
import plotly.graph_objects as go
import networkx as nx
from networkx import grid_graph
import random
import math
import globalvars
import pylab
import numpy as np

from itertools import combinations
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
from random import uniform
from numpy import pi, cos, sin, arccos, arange
import mpl_toolkits.mplot3d
########## spherical lattice
def ball_grid_points ( n, r, c, ng ):

#*****************************************************************************80
#
## ball_grid_points() computes grid points inside a ball.
#
#  Discussion:
#
#    The grid is defined by specifying the radius and center of the ball,
#    and the number of subintervals N into which the horizontal radius
#    should be divided.  Thus, a value of N = 2 will result in 5 points
#    along that horizontal line.
#
#
#  Input:
#
#    integer N, the number of subintervals.
#
#    real R, the radius of the ball.
#
#    real C(3), the coordinates of the center of the ball.
#
#    integer NG, the number of grid points, as determined by
#    ball_grid_count.
#
#  Output:
#
#    real BG(3,NG), the grid points inside the ball.
#
  import numpy as np

  bg = np.zeros ( ( ng, 3 ) )

  p = 0

  for i in range ( 0, n + 1 ):

    x = c[0] + r * float ( i ) / float ( n )

    for j in range ( 0, n + 1 ):

      y = c[1] + r * float ( j ) / float ( n )

      for k in range ( 0, n + 1 ):

        z = c[2] + r * float ( k ) / float ( n )

        if ( r * r < ( x - c[0] ) ** 2 \
                   + ( y - c[1] ) ** 2 \
                   + ( z - c[2] ) ** 2 ):
          break

        bg[p,0] = x
        bg[p,1] = y
        bg[p,2] = z
        p = p + 1

        if ( 0 < i ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = y
          bg[p,2] = z
          p = p + 1

        if ( 0 < j ):
          bg[p,0] = x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = z
          p = p + 1

        if ( 0 < k ):
          bg[p,0] = x
          bg[p,1] = y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

        if ( 0 < i and 0 < j ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = z
          p = p + 1

        if ( 0 < i and 0 < k ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

        if ( 0 < j and 0 < k ):
          bg[p,0] = x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

        if ( 0 < i and 0 < j and 0 < k ):
          bg[p,0] = 2.0 * c[0] - x
          bg[p,1] = 2.0 * c[1] - y
          bg[p,2] = 2.0 * c[2] - z
          p = p + 1

 # print("p is ",p)
  return bg

def r8mat_write ( filename, m, n, a ):

#*****************************************************************************80
#
## r8mat_write() writes an R8MAT to a file.
#
#  Input:
#
#    string FILENAME, the name of the output file.
#
#    integer M, the number of rows in A.
#
#    integer N, the number of columns in A.
#
#    real A(M,N), the matrix.
#
  output = open ( filename, 'w' )

  for i in range ( 0, m ):
    for j in range ( 0, n ):
      s = '  %g' % ( a[i,j] )
      output.write ( s )
      if j == 0:
          globalvars.node_loc[i]['x'] = a[i,j]
      if j == 1:
          globalvars.node_loc[i]['y'] = a[i,j]
      if j == 2:
          globalvars.node_loc[i]['z'] = a[i,j]

    output.write ( '\n' )

  output.close ( )

  return
#def ball_grid_display ( r, c, ng, xg, filename ):
#
#  import matplotlib.pyplot as plt
#  from mpl_toolkits.mplot3d import Axes3D
#
#  fig = plt.figure ( )
#  ax = fig.add_subplot ( 111, projection = '3d' )
#  ax.scatter ( xg[:,0], xg[:,1], xg[:,2], 'b' );
#
#  ax.set_xlabel ( '<---X--->' )
#  ax.set_ylabel ( '<---Y--->' )
#  ax.set_zlabel ( '<---Z--->' )
#  ax.set_title ( 'Grid points in ball' )
#  ax.grid ( True )
## ax.axis ( 'equal' )
#  plt.savefig ( filename )
#  plt.show ( block = False )
#
#  plt.close ( )
#
#  return

def ball_grid_points_test():

#*****************************************************************************80
#
## ball_grid_points_test() tests ball_grid_points().
#

#
  import numpy as np
  import platform
 # n = 2
  n = 4
 # n = 16
  r = 2.0
  #r = 4.0
 # r = 6.0
  c = np.array ( [ 1.0, 5.0, 2.0 ] )

  print ( '' )
  print ( '  We use N = %d' % ( n ) )
  print ( '  Radius R = %g' % ( r ) )
  print ( '  Center C = (%g,%g,%g)' % ( c[0], c[1], c[2] ) )
  
#  ng = 33
  ng = 257
 # ng = 2109
#  ng = 17077
 
  print ( '' )
  print ( '  Number of grid points will be %d' % ( ng ) )

  xg = ball_grid_points ( n, r, c, ng )

  filename = 'ball_grid_points.xyz'

  r8mat_write ( filename, ng, 3, xg )

##  Plot the grid.
##
#  filename = 'ball_grid_points.png'
#
#  ball_grid_display ( r, c, ng, xg, filename )

  return



def ball_grid_test ():

  import platform
  ball_grid_points_test()

#############
def source_destination_distance():
    
    ff = (globalvars.pos[globalvars.focus2_key][0]-globalvars.pos[globalvars.focus1_key][0])*(globalvars.pos[globalvars.focus2_key][0]-globalvars.pos[globalvars.focus1_key][0])+(globalvars.pos[globalvars.focus2_key][1]-globalvars.pos[globalvars.focus1_key][1])*(globalvars.pos[globalvars.focus2_key][1]-globalvars.pos[globalvars.focus1_key][1])+(globalvars.pos[globalvars.focus2_key][2]-globalvars.pos[globalvars.focus1_key][2])*(globalvars.pos[globalvars.focus2_key][2]-globalvars.pos[globalvars.focus1_key][2])
    focaldist = math.sqrt(ff)
    
    return focaldist


def magnitude(x):
 return math.sqrt(sum(i*i for i in x))

def calculate_backoff(location):

    '''returns backoff time in seconds'''

    ##extract the exact x,y,z coordinates
    x = location[0]
    y = location[1]
    z = location[2]
    t = (x,y,z) #t is the node for which backoff is calculated

    #ds is the directional vector of line joining points d (destination) and s (source)
    #calculated by subtracting dest coordinates from source coordinates 
    ds = tuple(map(lambda i, j: i - j, globalvars.packet['sLoc'], globalvars.packet['dLoc'] ))
    print("ds: ",ds)
    #dt is the directional vector of line joining d (destination) and t (node for which backoff is calculated)
    dt = tuple(map(lambda i, j: i - j, t, globalvars.packet['dLoc']))
    print("dt: ",dt)

    #To find: projection of vector dt_v on ds_v

    dt_v = np.array([dt[0],dt[1],dt[2]])
    ds_v = np.array([ds[0],ds[1],ds[2]])

    # finding norm of the vector ds_v
    #ds_v_norm = np.sqrt(sum(ds_v**2)) 
    numerator = np.dot(dt_v, ds_v)
    denominator = np.dot(ds_v, ds_v)
    # Apply the formula for projecting a vector onto another vector
    # find dot product using np.dot()
    proj_of_dtv_on_dsv = np.multiply((numerator/denominator),ds_v)
    #proj_of_dtv_on_dsv = (np.dot(dt_v, ds_v)/ds_v_norm**2)*ds_v
    

    print(proj_of_dtv_on_dsv)
    print(ds_v)
    #backoff time proportional to the distance from destination
    proj = magnitude(proj_of_dtv_on_dsv)
  #  tB1 = (globalvars.packet['tUB1'] * proj_of_dtv_on_dsv)/ds_v 
    tB1 = (globalvars.packet['tUB1'] * proj)/magnitude(ds_v) 
    print("tB1: ",tB1)
    #backoff time proportional to the distance from source-destination line
    print("mag dt_v sq: ",(magnitude(dt_v))**2)
    print("mag : proj_of_dtv_on_dsv sq",(magnitude(proj_of_dtv_on_dsv))**2)
    orthogonal_dist = math.sqrt((magnitude(dt_v))**2 - (magnitude(proj_of_dtv_on_dsv))**2)
    print("orth dist: ",orthogonal_dist)
    tB2 = (globalvars.packet['tUB2'] * orthogonal_dist)/source_destination_distance() 
    print("s d dist: ",source_destination_distance())
  #  print("tB2: ",tB2)


    backofftime = tB1 + tB2
 #   backofftime = magnitude(backofftime)

    return backofftime

def find_centroid(received_from_location):
    x = [p[0] for p in received_from_location]
    y = [p[1] for p in received_from_location]
    z = [p[2] for p in received_from_location]
    centroid = (sum(x) / len(received_from_location), sum(y) / len(received_from_location), sum(z)/len(received_from_location))

    print("centroid",centroid)

    return centroid


def compare_distance_to_destination(centroid,mylocation,destlocation):
    x1 = centroid[0]
    y1 = centroid[1]
    z1 = centroid[2]

    xd = destlocation[0]
    yd = destlocation[1]
    zd = destlocation[2]
    
    x2 = mylocation[0]
    y2 = mylocation[1]
    z2 = mylocation[2]
    
    
    dif = ((xd - x1 )**2) + ((yd-y1)**2) + ((zd-z1)**2)
    centroiddist = math.sqrt(dif)

    dif1 = ((xd - x2)**2) + ((yd-y2)**2) + ((zd-z2)**2)
    mydist = math.sqrt(dif1)
    print("dist from centroid",centroiddist) 
    print("dist from my location",mydist) 

    if centroiddist > mydist:
        return 1
    else:
        return 0




def insideOrNot(location):

    #extract the exact x,y,z coordinates
    
    x = location[0]
    y = location[1]
    z = location[2]
        
    #eq of the ellipsoid centered at (h,k,f)

    h= (globalvars.pos[globalvars.focus1_key][0]+globalvars.pos[globalvars.focus2_key][0])/2
    k= (globalvars.pos[globalvars.focus1_key][1]+globalvars.pos[globalvars.focus2_key][1])/2
    f= (globalvars.pos[globalvars.focus1_key][2]+globalvars.pos[globalvars.focus2_key][2])/2
    sol = (x-h)*(x-h)/(globalvars.a*globalvars.a) + (y-k)*(y-k)/(globalvars.b*globalvars.b) + (x-f)*(x-f)/(globalvars.c*globalvars.c)
    #semi axes are of lengths a, b, c

    if sol <= 1:
        return 1 #inside
    else:
        return 0



def initiate_source_destination():
    
    print("SOURCE AND DESTINATION")
    print("------------------------")
    all_position_keys = []
    all_position_keys = list(globalvars.pos.keys())
    #print(all_position_keys)
    globalvars.focus1_key = np.random.choice(all_position_keys)
    
    while True:
        globalvars.focus2_key = np.random.choice(all_position_keys)
        if globalvars.focus1_key != globalvars.focus2_key:
            break
   
    
    print("source:",globalvars.focus1_key)
    print("destination:",globalvars.focus2_key)
    initiate_petal_parameters()




def initiate_petal_parameters():

    print("PETAL PARAMETERS")
    print("----------------")
    
    print("Coordinates of focus 1 (source): (", globalvars.pos[globalvars.focus1_key][0],",", globalvars.pos[globalvars.focus1_key][1],",", globalvars.pos[globalvars.focus1_key][2],")" )
    print("Coordinates of focus 2 (destination): (", globalvars.pos[globalvars.focus2_key][0],",", globalvars.pos[globalvars.focus2_key][1],",", globalvars.pos[globalvars.focus2_key][2],")" )
    globalvars.packet['sLoc'] = (globalvars.pos[globalvars.focus1_key][0], globalvars.pos[globalvars.focus1_key][1], globalvars.pos[globalvars.focus1_key][2])
    globalvars.packet['dLoc'] = (globalvars.pos[globalvars.focus2_key][0], globalvars.pos[globalvars.focus2_key][1], globalvars.pos[globalvars.focus2_key][2])


    ff = (globalvars.pos[globalvars.focus2_key][0]-globalvars.pos[globalvars.focus1_key][0])**2 +(globalvars.pos[globalvars.focus2_key][1]-globalvars.pos[globalvars.focus1_key][1])**2+(globalvars.pos[globalvars.focus2_key][2]-globalvars.pos[globalvars.focus1_key][2])**2
    focaldist = math.sqrt(ff)
    print("Distance between two foci =", focaldist)
    print("Linear eccentricity =", focaldist/2)
    print("Centre of ellipsoid = (", (globalvars.pos[globalvars.focus1_key][0]+globalvars.pos[globalvars.focus2_key][0])/2,",",(globalvars.pos[globalvars.focus1_key][1]+globalvars.pos[globalvars.focus2_key][1])/2,",",(globalvars.pos[globalvars.focus1_key][2]+globalvars.pos[globalvars.focus2_key][2])/2,")")

    print("Eccentricity:",globalvars.e)
    #is that of the ellipse formed by a section containing both the longest and the shortest axes (one of which will be the polar axis (x axis))
    globalvars.a = focaldist/(2*globalvars.e)
    print("Semi major axis, a = ", globalvars.a)

    ma = globalvars.a+globalvars.a
    print("major axis, a+a = ", ma)
    globalvars.b = globalvars.a * math.sqrt(1-(globalvars.e)**2)
    print("Semi minor axis, b = ", globalvars.b)
    print("minor axis, b = ", globalvars.b+ globalvars.b)
    if focaldist > ma:
        print("incorrect")
    #globalvars.c = random.uniform(globalvars.b,globalvars.c)
    # a = b = c: sphere
    # a = b > c: oblate spheroid.
    # a = b < c: prolate spheroid
    # a > b > c: scalene spheroid or triaxial.
    globalvars.c = random.uniform(0,globalvars.b)
    print("c = ",globalvars.c)



def generate_adjlist_with_all_edges(G,delimiter):
    for s, nbrs in G.adjacency():
        line = str(s) + delimiter
        for t, data in nbrs.items():
            line += str(t) + delimiter
        yield line[: -len(delimiter)]

def distance(u, v):
    x1 = globalvars.pos[u][0]
    x2 = globalvars.pos[v][0]
    y1 = globalvars.pos[u][1]
    y2 = globalvars.pos[v][1]
    z1 = globalvars.pos[u][2]
    z2 = globalvars.pos[v][2]
    
    dd = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2-z1)*(z2-z1)
    d = math.sqrt(dd)
    return d

def distance_between_nodes(u, v):
    x1 = globalvars.node_loc[u]['x']
    x2 = globalvars.node_loc[v]['x']
    y1 = globalvars.node_loc[u]['y']
    y2 = globalvars.node_loc[v]['y']
    z1 = globalvars.node_loc[u]['z']
    z2 = globalvars.node_loc[v]['z']
    
    dd = (x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2-z1)*(z2-z1)
    d = math.sqrt(dd)
    return d

def generate_random_3Dgraph(n_nodes, radius, seed=None):

    if seed is not None:
        random.seed(seed)
   
    globalvars.node_loc = [{'x':0, 'y':0, 'z':0} for i in range(0,globalvars.number_of_nodes+1)]

    #wireless range: 25 to 50 feet
    #4 units of distance is 100 feet
    #Total area is 1000 x 1000 x 1000 cubic feet
    
   
#    if globalvars.topology == 0: #Perfect Lattice
#        n = 0
#        side = int((globalvars.number_of_nodes+1)**(1.0/3))
#        print(globalvars.number_of_nodes)
#        print(side)
#        while n < globalvars.number_of_nodes:
#            for i in range(1,side+1):
#                for j in range(1,side+1):
#                    for k in range(1,side+1):
#                        node_loc[n]['x'] = i
#                        node_loc[n]['y'] = j
#                        node_loc[n]['z'] = k
#                        n += 1
#

#    if globalvars.topology == 2: #Spherical Lattice
#       diameter = 6 #number of points along diameter, two consecutive points a unit distance apart
#      # radius = diameter/2
#       n = 0
#
#       while n < globalvars.number_of_nodes:
#        ctr = diameter
#        #points along x axis
#        while ctr > 0:
#            node_loc[n]['x'] = ctr
#            node_loc[n]['y'] = 0
#            node_loc[n]['z'] = 0
#            ctr = ctr-1
#            n +=1
#        ctr = diameter
#        #points along y axis
#        while ctr > 0:
#            node_loc[n]['x'] = 0
#            node_loc[n]['y'] = ctr
#            node_loc[n]['z'] = 0
#            ctr = ctr-1
#            n +=1
#        ctr = diameter
#        #points along x axis
#        while ctr > 0:
#            node_loc[n]['x'] = 0
#            node_loc[n]['y'] = 0
#            node_loc[n]['z'] = ctr
#            ctr = ctr-1
#            n +=1


    if globalvars.topology == 2: #Spherical Lattice
        ball_grid_test()



  #  if globalvars.topology == 1: #Perturbed Lattice
  #      n = 0
  #      side = int((globalvars.number_of_nodes+1)**(1.0/3))
  #      print(globalvars.number_of_nodes)
  #      print(side)
  #      while n < globalvars.number_of_nodes:
  #          for i in range(1,side+1):
  #              for j in range(1,side+1):
  #                  for k in range(1,side+1):
  #                      perturbation = random.randint(0,1)
  #                      node_loc[n]['x'] = i + perturbation
  #                      perturbation = random.randint(0,1)
  #                      node_loc[n]['y'] = j + perturbation
  #                      perturbation = random.randint(0,1)
  #                      node_loc[n]['z'] = k + perturbation
  #                      n += 1


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
                        globalvars.node_loc[n]['x'] = i + noise[n]
                        globalvars.node_loc[n]['y'] = j + noise[n]
                        globalvars.node_loc[n]['z'] = k + noise[n]
                        n += 1

 #   if globalvars.topology == 2: #Sphere
 #       n = 0
 #       print(globalvars.number_of_nodes)
 #       while n < globalvars.number_of_nodes:
 #           x = uniform(-1,1);
 #           y = uniform(-1,1);
 #           z = uniform(-1,1);
 #           mag = math.sqrt( (x*x) + (y*y) + (z*z) );
 #           d = uniform(0,1) / mag;
 #           x *= d;
 #           y *= d;
 #           z *= d;
 #           node_loc[n]['x'] = x
 #           node_loc[n]['y'] = y
 #           node_loc[n]['z'] = z
 #           #print("x=",x,"y=",y,"z=",z)
 #           n += 1

  #  if globalvars.topology == 2: #Sphere
  #      n = 0
  #      while n < globalvars.number_of_nodes:
  #          theta = uniform(0,1) * 2.0*3.14;
  #          phi = uniform(0,1) * 3.14
  #          r = uniform(0,1)
  #          sinTheta = math.sin(theta)
  #          cosTheta = math.cos(theta);
  #          sinPhi = math.sin(phi)
  #          cosPhi = math.cos(phi)
  #          x = r * sinPhi * cosTheta
  #          y = r * sinPhi * sinTheta
  #          z = r * cosPhi
  #          node_loc[n]['x'] = x
  #          node_loc[n]['y'] = y
  #          node_loc[n]['z'] = z
  #          n += 1

    # Generate a dict of positions
    position = {i: (globalvars.node_loc[i]['x'], globalvars.node_loc[i]['y'], globalvars.node_loc[i]['z']) for i in range(n_nodes)}

 
    # Create random 3D network
   # g = nx.random_geometric_graph(n_nodes, radius, pos=position)
   # print(g.edges())
    globalvars.G = nx.random_geometric_graph(n_nodes, radius, pos=position)
    globalvars.pos = nx.get_node_attributes(globalvars.G, 'pos')
    print("Position of all nodes initially: ",globalvars.pos) 




    to_del = []
    for u, v in combinations(globalvars.G, 2):
      dist = distance_between_nodes(u,v)
      #print(dist)
      if dist <= 0.4: #if distance is less than 10 feet
         # print("distance=",dist," : nodes are too close, removing")
          to_del.append(u)
          to_del.append(v)
          continue
      if dist >= 0.8: #if distance is more than 20 feet
          pass
      elif dist < 0.6: #if distance is less than 15 feet
       #   print(dist)
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
    #    for i,j in enumerate(G.edges()):

    #        x = np.array((globalvars.pos[j[0]][0], globalvars.pos[j[1]][0]))
    #        y = np.array((globalvars.pos[j[0]][1], globalvars.pos[j[1]][1]))
    #        z = np.array((globalvars.pos[j[0]][2], globalvars.pos[j[1]][2]))
    #    
    #    # Plot the connecting lines
    #        ax.plot(x, y, z, c='black', alpha=0.5)
    
    # Set the initial view
    ax.view_init(30, angle)

    # Hide the axes
    ax.set_axis_off()

    plt.show()
    
    return


def create_drones_network():


    n = globalvars.number_of_nodes  
    G = generate_random_3Dgraph(n_nodes=n, radius=0.25, seed=1)
    network_plot_3D(G,0, save=False)
    

    x_nodes = [globalvars.pos[key][0] for key in globalvars.pos.keys()]
    y_nodes = [globalvars.pos[key][1] for key in globalvars.pos.keys()]
    z_nodes = [globalvars.pos[key][2] for key in globalvars.pos.keys()]
    
    #assign node id to each coordinate
    globalvars.node = [{'nodeID':0, 'loc':(0,0,0), 'packet':0} for i in range(globalvars.number_of_nodes)]
    for i in range(globalvars.number_of_nodes):
        globalvars.node[i]['nodeID'] = i
        globalvars.node[i]['loc'] = (x_nodes[i],y_nodes[i],z_nodes[i])
        globalvars.node[i]['packet'] = 0
    print("NODES")
    print("----------------")
    #print(globalvars.node)

   
    #update number of nodes
    globalvars.number_of_nodes = len(globalvars.G.nodes())
    #make adj list correct (both directions) 
    print("ADJACENCY LIST")
    print("----------------")

  #  for line in generate_adjlist_with_all_edges(globalvars.G,' '):
  #      print(line)
