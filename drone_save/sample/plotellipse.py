#https://newbedev.com/plot-ellipse-with-matplotlib-pyplot-python

import numpy as np
import matplotlib.pyplot as plt
from math import pi

#equation of ellipse 
# (x-u)**2/a**2 + (y-v)**2/b**2 = 1
#(u,v) is the centre of the ellipse

#parametric equation of an ellipse

#x= u+ acos(t); y = v +b sin(t)


u=1.     #x-position of the center
v=0.5    #y-position of the center
a=2.     #radius on the x-axis
b=1.5    #radius on the y-axis

t = np.linspace(0, 2*pi, 100)
plt.plot( u+a*np.cos(t) , v+b*np.sin(t) )
plt.grid(color='lightgray',linestyle='--')
plt.show()
