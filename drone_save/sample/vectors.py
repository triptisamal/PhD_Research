import math

theta = 0
theta1 = 0
u = []

def R():
    
    global theta
    global u
    return [[round(math.cos(theta),2) + u[0]**2 * (1-round(math.cos(theta),2)), 
             u[0] * u[1] * (1-round(math.cos(theta),2)) - u[2] * round(math.sin(theta),2), 
             u[0] * u[2] * (1 - round(math.cos(theta),2)) + u[1] * round(math.sin(theta),2)],
            [u[0] * u[1] * (1-round(math.cos(theta),2)) + u[2] * round(math.sin(theta),2),
             round(math.cos(theta),2) + u[1]**2 * (1-round(math.cos(theta),2)),
             u[1] * u[2] * (1 - round(math.cos(theta),2)) - u[0] * round(math.sin(theta),2)],
            [u[0] * u[2] * (1-round(math.cos(theta),2)) - u[1] * round(math.sin(theta),2),
             u[1] * u[2] * (1-round(math.cos(theta),2)) + u[0] * round(math.sin(theta),2),
             round(math.cos(theta),2) + u[2]**2 * (1-round(math.cos(theta),2))]]



def magnitude(vect):
    return math.sqrt((vect[0])**2+(vect[1])**2+(vect[2])**2)

            
def R_z(direction):
    global theta1
    if direction == 0:#clockwise
        return [[round(math.cos(theta1),2),round(math.sin(theta1),2),0],
            [-round(math.sin(theta1),2),round(math.cos(theta1),2),0],
            [0,0,1]]
    if direction == 1:#anticlockwise
        return [[round(math.cos(theta1),2),-round(math.sin(theta1),2),0],
            [round(math.sin(theta1),2),round(math.cos(theta1),2),0],
            [0,0,1]]

def R_x(direction):
    
    global theta

    if direction == 0: #clockwise
        return [[1,0,0],
             [0,round(math.cos(theta),2), round(math.sin(theta),2)],
            [0,-round(math.sin(theta),2),  round(math.cos(theta),2)]]
    if direction == 1: #anticlockwise
        return [[1,0,0],
             [0,round(math.cos(theta),2),-round(math.sin(theta),2)],
            [0,round(math.sin(theta),2),round(math.cos(theta),2)]]
            
            
def rotatez(pointToRotate,direction):


    global theta1

    r = R_z(direction)

    rotated = []

    for j in range(3):
        summ=0
        for i in range(3):
            #print(pointToRotate[i],"*",r[j][i])
            summ += pointToRotate[i]*r[j][i]
        rotated.append(round(summ))

    return rotated

def rotate(pointToRotate,direction):


    r = R_x(direction)

    rotated = []
    

    for j in range(3):
        summ=0
        for i in range(3):
           # print(pointToRotate[i],"*",r[j][i])
            summ += pointToRotate[i]*r[j][i]
        rotated.append(round(summ))


    return rotated


def if_different_zsign(s,d):

    if s[2]>0 and d[2]<0:
        return 1
    elif s[2]<0 and d[2]>0:
        return 1
    else:
        return 0


def find_direction(s):
    
    if s[0]>0 and s[1]>0 and s[2]>0:#+++
        return 0
    elif s[0]<0 and s[1]<0 and s[2]<0:#---
        return 1
    elif s[0]>0 and s[1]<0 and s[2]>0:#+-+
        return 1
    elif s[0]>0 and s[1]>0 and s[2]<0:#++-
        return 0
    elif s[0]>0 and s[1]<0 and s[2]<0:#+--
        return 1
    elif s[0]<0 and s[1]>0 and s[2]<0:#-+-
        return 0
    elif s[0]<0 and s[1]<0 and s[2]>0:#--+
        return 1
    else:#-++
        return 0

#Not using yet
#def normal_round(n, decimals=0):
#    expoN = n * 10 ** decimals
#    if abs(expoN) - abs(math.floor(expoN)) < 0.5:
#        return math.floor(expoN) / 10 ** decimals
#    return math.ceil(expoN) / 10 ** decimals
def my_round(n, ndigits):
    part = n * 10 ** ndigits
    delta = part - int(part)
    # always round "away from 0"
    if delta >= 0.5 or -0.5 < delta <= 0:
        part = math.ceil(part)
    else:
        part = math.floor(part)
    return part / (10 ** ndigits) if ndigits >= 0 else part * 10 ** abs(ndigits)

def main():

    global theta
    global theta1
    #correct
    #-+
    s = [3,-4,-5]
    d = [5,5,7]
    
    sd_vector=[d[0]-s[0],d[1]-s[1],d[2]-s[2]]
    print(sd_vector)

    #angle between sd_vector and xy plane theta
    iz_vector = [0,0,1]
    iy_vector = [0,1,0]
    ix_vector = [1,0,0]


    #Angle between position vector of s and xy plane
    theta = math.acos((s[0]*iz_vector[0]+s[1]*iz_vector[1]+s[2]*iz_vector[2])/(magnitude(s)*magnitude(iz_vector)))
    #theta = (sympy.pi)/2-theta
    theta = 1.5708-theta
    direction=find_direction(s)
    
    if(if_different_zsign(s,d)):
        theta=theta+3.14159
    print("Angle between position vector of s and xy plane=",math.degrees(theta))
    _s = rotate(s,direction)
    print("s=",s,"_s=",_s)
    
    #Angle between position vector of d and xy plane
    theta = math.acos((d[0]*iz_vector[0]+d[1]*iz_vector[1]+d[2]*iz_vector[2])/(magnitude(d)*magnitude(iz_vector)))
    theta = 1.5708-theta
    #theta = (sympy.pi)/2-theta
    direction=find_direction(d)
   # #theta=0.9
    print("Angle between position vector of d and xy plane=",math.degrees(theta))
    
    _d = rotate(d,direction)
    print("d=",d,"_d=",_d)

    sd_rotated = [_d[0]-_s[0],_d[1]-_s[1],_d[2]-_s[2]]
    print("sd_rotated (in plane xy)=",sd_rotated)

    #angle between rotated vector and z axis
    theta2 = math.acos((sd_rotated[0]*iz_vector[0]+sd_rotated[1]*iz_vector[1]+sd_rotated[2]*iz_vector[2])/(magnitude(sd_rotated)*magnitude(iz_vector)))
    print("For testing: Angle between rotated vector sd (in xy plane) and z-axis=",math.degrees(theta2))
    
    
    #Angle between position vector of sd_rotated and x axis
    theta1 = math.acos((sd_rotated[0]*ix_vector[0]+sd_rotated[1]*ix_vector[1]+sd_rotated[2]*ix_vector[2])/(magnitude(sd_rotated)*magnitude(ix_vector)))
    print("Angle between position vector of sd_rotated and x axis=",math.degrees(theta))
    
    
    if (sd_rotated[0]>0 and sd_rotated[1]<0):
        direction=1 #anticlockwise

    if (sd_rotated[0]<0 and sd_rotated[1]>0):
        direction=0 #clockwise
    
    if (sd_rotated[0]>0 and sd_rotated[1]>0):
        direction=0 #clockwise
    
    if (sd_rotated[0]<0 and sd_rotated[1]<0):
        direction=1 #anticlockwise



    __s = rotatez(_s,direction)
    print("_s=",_s,"__s=",__s)

    __d = rotatez(_d,direction)
    print("_d=",_d,"__d=",__d)


    finalsd_rotated = [__d[0]-__s[0],__d[1]-__s[1],__d[2]-__s[2]]

    print("Final sd_vector=",finalsd_rotated)

    alp = math.acos((finalsd_rotated[0]*ix_vector[0]+finalsd_rotated[1]*ix_vector[1]+finalsd_rotated[2]*ix_vector[2])/(magnitude(finalsd_rotated)*magnitude(ix_vector)))
    print("Angle with x axis=",math.degrees(alp))

    #angle between sd_vector and y axis phi
    phi = math.acos((finalsd_rotated[0]*iy_vector[0]+finalsd_rotated[1]*iy_vector[1]+finalsd_rotated[2]*iy_vector[2])/(magnitude(finalsd_rotated)*magnitude(iy_vector)))
    print("Angle with y axis=",math.degrees(phi))

    #angle between sd_vector and z axis alpha
    alpha = math.acos((finalsd_rotated[0]*iz_vector[0]+finalsd_rotated[1]*iz_vector[1]+finalsd_rotated[2]*iz_vector[2])/(magnitude(finalsd_rotated)*magnitude(iz_vector)))

    print("Angle with z axis=",math.degrees(alpha))
   
    print("Original sd=",sd_vector)
    print("Rotated sd=",finalsd_rotated)
    
    v = [sd_vector[1]*finalsd_rotated[2]+sd_vector[2]*finalsd_rotated[1],sd_vector[2]*finalsd_rotated[0]+sd_vector[0]*finalsd_rotated[2],sd_vector[0]*finalsd_rotated[1]+sd_vector[1]*finalsd_rotated[0]]

    #Normalize the cross product to a unit vector u
    u = [v[0]/magnitude(v),v[1]/magnitude(v),v[2]/magnitude(v)]
    

    angle = math.acos((finalsd_rotated[0]*sd_vector[0]+finalsd_rotated[1]*sd_vector[1]+finalsd_rotated[2]*sd_vector[2])/(magnitude(finalsd_rotated)*magnitude(sd_vector)))
    print("Angle angle between final and initial sd=",math.degrees(angle))


if __name__=="__main__":
    main()

