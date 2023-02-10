from random import uniform
import math

count=0
while count < 10:
    x = uniform(-1,1);
    y = uniform(-1,1);
    z = uniform(-1,1);
    mag = math.sqrt( (x*x) + (y*y) + (z*z) );
    d = uniform(0,1) / mag;
    x *= d;
    y *= d;
    z *= d;
    print("x=",x,"y=",y,"z=",z)
    count += 1
