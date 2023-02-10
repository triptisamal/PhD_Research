import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)


x = np.linspace(-9, 9, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)
a = 4.
b = 2.
axes()
plt.contour(x, y,(x**2/a**2 + y**2/b**2), [1], colors='k')
plt.show()
