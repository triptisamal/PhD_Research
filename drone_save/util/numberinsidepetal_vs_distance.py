import numpy as np
import matplotlib.pyplot as plt
y = []
with open("petal_numberinsidepetal_216_0.400000.txt", "r") as f:
    for line in f:
        line = line.strip()
        y.append(int(line))

x = []
with open("petal_sourcedestdistance_216_0.400000.txt", "r") as f:
    for line in f:
        line = line.strip()
        x.append(float(line))

arr = np.array(x)
arr=arr*25
plt.figure(figsize=(12, 5))
plt.title('Total Number of Nodes = 216, Topology = Lattice, Shape = Cuboid, e = 0.9',fontsize=16)
plt.suptitle('Distance between Source and Destination vs Number of nodes inside Petal',fontsize=24, y=1)
plt.xlabel("Source Destination Distance (feet)")
plt.ylabel("Number of nodes inside the Petal")
plt.scatter(arr,y)
plt.show()
