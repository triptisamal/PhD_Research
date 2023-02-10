# Import libraries
import matplotlib.pyplot as plt
import numpy as np


# Creating dataset
np.random.seed(10)
data = (1.4142135623730951 ,
3.7416573867739413 ,
6.4031242374328485 ,
3.7416573867739413 ,
7.810249675906654 ,
3.0 ,
0 ,
5.744562646538029 ,
2.8284271247461903 ,
5.385164807134504 ,
5.830951894845301 ,
4.47213595499958 ,
6.782329983125268 ,
0 ,
4.123105625617661 ,
0 ,

5.0990195135927845 ,
1.4142135623730951 ,
6.164414002968976 ,
3.0 ,
1.7320508075688772 ,
8.54400374531753 ,
4.123105625617661 ,
4.58257569495584 ,
5.916079783099616 ,
4.358898943540674 ,
6.164414002968976 ,
0 ,
3.0 ,
0 ,
0,
100)


arr1=np.array(data)
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


# boxplot of data within the whisker
arr2 = arr1[(arr1 >= lower_bound) & (arr1 <= upper_bound)]
plt.figure(figsize=(12, 7))
plt.boxplot(arr1)
plt.show()
