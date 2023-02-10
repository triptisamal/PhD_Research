
from numpy import pi, cos, sin, arccos, arange
import mpl_toolkits.mplot3d
import matplotlib.pyplot as pp
import networkx as nx
from itertools import combinations
import math
import random
#3D sphere

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

##generate points positions

num_pts = 200
indices = arange(0, num_pts, dtype=float) + 0.5
phi = arccos(1 - 2*indices/num_pts)
theta = pi * (1 + 5**0.5) * indices

x, y, z = cos(theta) * sin(phi), sin(theta) * sin(phi), cos(phi);
pp.figure().add_subplot(111, projection='3d').scatter(x, y, z);
pp.show()

node_loc = [{'x':0, 'y':0, 'z':0} for i in range(200)]

##Generate networkx graphs with the given positions
g = nx.Graph()
for key in range(num_pts):
    g.add_node(key,pos=(x[key],y[key],z[key]))
  #  if key > 1:
  #      g.add_edge(key,key-1)
    node_loc[key]['x'] = x[key]
    node_loc[key]['y'] = y[key]
    node_loc[key]['z'] = z[key]
#for n in range(200):
#     for rl in range(200):
#         # Check the distance, if < d, generate edge
#         if distance(n, rl, node_loc) < 0.2:
#             # add edge
#             g.add_edge(n,rl)
##to_del = []
#for u, v in combinations(g, 2):
#  dist = distance(u,v,node_loc)
# # if dist <= 0.001:
# #     print("distance=",dist," : nodes are too close, removing")
# #     to_del.append(u)
# #     to_del.append(v)
# #     continue
#  if dist >= 0.25:
#      pass
#  elif dist < 0.09:
#      g.add_edge(u, v)
#  else:
#      p = 1 - ((dist - 0.09)/0.16)
#      q = random.uniform(0,1)
#      if q <= p:
#          g.add_edge(u, v)
##g.remove_nodes_from(to_del)


pos=nx.get_node_attributes(g,'pos')
print(pos)
nx.draw(g,pos)
pp.show()
##2D circle
#from numpy import pi, cos, sin, sqrt, arange
#import matplotlib.pyplot as pp
#
#num_pts = 100
#indices = arange(0, num_pts, dtype=float) + 0.5
#
#r = sqrt(indices/num_pts)
#theta = pi * (1 + 5**0.5) * indices
#
#pp.scatter(r*cos(theta), r*sin(theta))
#pp.show()
