from math import pi ,sin, cos

def R(theta, u):
    print(u[0])
    print(u[1])
    print(u[2])
    print(u[1] * round(sin(theta),2))
    return [[round(cos(theta),2) + u[0]**2 * (1-round(cos(theta),2)), 
             u[0] * u[1] * (1-round(cos(theta),2)) - u[2] * round(sin(theta),2), 
             u[0] * u[2] * (1 - round(cos(theta),2)) + u[1] * round(sin(theta),2)],
            [u[0] * u[1] * (1-round(cos(theta),2)) + u[2] * round(sin(theta),2),
             round(cos(theta),2) + u[1]**2 * (1-round(cos(theta),2)),
             u[1] * u[2] * (1 - round(cos(theta),2)) - u[0] * round(sin(theta),2)],
            [u[0] * u[2] * (1-round(cos(theta),2)) - u[1] * round(sin(theta),2),
             u[1] * u[2] * (1-round(cos(theta),2)) + u[0] * round(sin(theta),2),
             round(cos(theta),2) + u[2]**2 * (1-round(cos(theta),2))]]

def Rotate(pointToRotate, theta):
#def Rotate(pointToRotate, point1, point2, theta):


#    u= []
#    squaredSum = 0
#    for i,f in zip(point1, point2):
#        u.append(f-i)
#        squaredSum += (f-i) **2
#
#    u = [i/squaredSum for i in u]
    u = [0,0.894,-0.447]
    r = R(theta, u)

    print(r)
    rotated = []
    

    for j in range(3):
        summ=0
        for i in range(3):
            print(pointToRotate[j],"*",r[j][i])
            summ += pointToRotate[j]*r[j][i]
        rotated.append(round(summ))

#    for i in range(3):
#        rotated.append(round(sum([r[j][i] * pointToRotate[j] for j in range(3)])))
#
    return rotated


point = [3,3,3]
#point = [1,0,0]
#p1 = [0,0,0]
#p2 = [0,1,0]

print(Rotate(point, 1.5708)) # [-1.0, 0.0, 0.0]
#print(Rotate(point, p1, p2, 1.5708)) # [-1.0, 0.0, 0.0]

