import numpy as np
from scipy.special import gammainc
from matplotlib import pyplot as plt


def sample(center,radius,n_per_sphere):
    r = radius
    ndim = center.size
    print(ndim)
    x = np.random.normal(size=(n_per_sphere, ndim))
    ssq = np.sum(x**2,axis=1)
    fr = r*gammainc(ndim/2,ssq/2)**(1/ndim)/np.sqrt(ssq)
    frtiled = np.tile(fr.reshape(n_per_sphere,1),(1,ndim))
    p = center + np.multiply(x,frtiled)
    return p

fig1 = plt.figure(1)
ax1 = fig1.gca()
center = np.array([0,0,0])
radius = 1
p = sample(center,radius,200)
ax1.scatter(p[:,0],p[:,1],s=0.5)
ax1.add_artist(plt.Circle(center,radius,fill=False,color='0.5'))
ax1.set_xlim(-1.5,1.5)
ax1.set_ylim(-1.5,1.5)
ax1.set_aspect('equal')
plt.show()

