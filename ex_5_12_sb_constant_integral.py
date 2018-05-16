from math import pi
from scipy.integrate import quad
from scipy.constants import c,hbar,k
from numpy import exp,inf

T = 300
a = 0
b = inf
e = 2.718281

def f(x):
    return (x**3)/((exp(x)) - 1)

W = (((k**4)*(T**4)) / ((4*pi**2)*(c**2)*(hbar**3))) * quad(f,a,b,epsabs=0)[0]


sb = W / (T**4)

print(W)
print(sb)