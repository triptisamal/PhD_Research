# import numpy to perform operations on vector
import numpy as np

u = np.array([1, 2, 3]) # vector u
v = np.array([5, 6, 2]) # vector v:

# Task: Project vector u on vector v

# finding norm of the vector v
v_norm = np.sqrt(sum(v**2))	

# Apply the formula as mentioned above
# for projecting a vector onto another vector
# find dot product using np.dot()
proj_of_u_on_v = (np.dot(u, v)/v_norm**2)*v

print("Projection of Vector u on Vector v is: ", proj_of_u_on_v)

