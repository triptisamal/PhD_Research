import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

bcast = []
with open("petal_numberinsidepetal_64_0.900000.txt", "r") as f:
    for line in f:
        line = line.strip()
        bcast.append(int(line))
arr1=np.array(bcast)
print("max tx=",np.amax(arr1))
count = np.count_nonzero(arr1 == np.amax(arr1))
print("max tx happened",count,"times")
print("max tx where=",np.where(arr1==np.amax(arr1)))
# finding the 1st quartile
q1 = np.quantile(arr1, 0.25)
# finding the 3rd quartile
q3 = np.quantile(arr1, 0.75)
med = np.median(arr1)
# finding the iqr region
iqr = q3-q1
# finding upper and lower whiskers
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)
#print(iqr, upper_bound, lower_bound)


outliers = arr1[(arr1 <= lower_bound) | (arr1 >= upper_bound)]
print('The following are the outliers in the boxplot:',outliers)
bcast1 = []
with open("petal_numberofbcast_64_0.900000_0.txt", "r") as f1:
    for line in f1:
        line = line.strip()
        bcast1.append(int(line))
arrayb=np.array(bcast1)

for i in range(len(outliers)):
    #print(outliers[i])
    print(np.where(arr1==outliers[i]))
    print(np.where(arrayb==outliers[i]))

data = np.array([arr1]) 
data = data.transpose()
df = pd.DataFrame(data, columns = ['64'])
plt.figure(figsize=(12, 7))
plt.title('Topology = Cubic Lattice, e = 0.9, Number of observations = 500',fontsize=23)
plt.suptitle('Distribution of Number of Nodes inside Petal',fontsize=25, y=1)
plt.xlabel("Number of Nodes",fontsize=23)
plt.ylabel("Number of Nodes inside Petal",fontsize=23)
plt.ylim=((0,22.5))
df.boxplot(showmeans=True)
plt.show()
