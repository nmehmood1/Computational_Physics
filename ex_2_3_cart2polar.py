# Simple program to convert cartesian coordinates to polar
from math import sqrt,atan
def c2p(x,y):
    r = sqrt(x**2 + y**2)
    theta = 57.3*atan(y/x)
    return [r,theta]

x = int(input('Enter an x value.'))
y = int(input('Enter a y value.'))

print(c2p(x,y))