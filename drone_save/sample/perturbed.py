import pandas as pd
# create a sample dataset with dimension (2,2)
# in your case you need to replace this with 
# clean_signal = pd.read_csv("your_data.csv")   
clean_signal = pd.DataFrame([[1,2],[3,4]], columns=list('AB'), dtype=float) 
print(clean_signal)
"""
print output: 
    A    B
0  1.0  2.0
1  3.0  4.0
"""
import numpy as np 
mu, sigma = 0, 0.1 
# creating a noise with the same dimension as the dataset (2,2) 
noise = np.random.normal(mu, sigma, [2,2]) 
print(noise)

"""
print output: 
array([[-0.11114313,  0.25927152],
       [ 0.06701506, -0.09364186]])
"""
signal = clean_signal + noise
print(signal)
"""
print output: 
          A         B
0  0.888857  2.259272
1  3.067015  3.906358
""" 

