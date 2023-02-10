# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data1 = []
with open("petal_numberofbcast_216_0.400000_0.txt", "r") as f:
    for line in f:
        line = line.strip()
        data1.append(int(line))

arr1=np.array(data1)
print("max tx=",np.amax(arr1))
print("max tx=",np.where(arr1==212))
print("min tx where=",np.where(arr1==1))
print("=",arr1[74])

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
print(iqr, upper_bound, lower_bound)


outliers = arr1[(arr1 <= lower_bound) | (arr1 >= upper_bound)]
print('The following are the outliers in the boxplot:',format(outliers))
data = np.array([arr1]) 
data = data.transpose()
df = pd.DataFrame(data, columns = ['216'])
plt.figure(figsize=(12, 7))
plt.title('Topology = Cubic Lattice, Number of observations = 500',fontsize=16)
plt.suptitle('Distribution of Transmissions',fontsize=24, y=1)
plt.xlabel("Number of Nodes")
plt.ylabel("Number of Transmissions")
df.boxplot(showmeans=True)
plt.show()
