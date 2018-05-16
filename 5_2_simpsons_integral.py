# program comparing trapezium method and simpson method of integration w/ N = 10 slices to sciPy quad method.

from scipy.integrate import quad

def f(x):
    return x**4 - 2*x + 1

N = 10
a = 0.0
b = 2.0
h = (b-a)/N
trueValue = 4.4
simp = f(a) + f(b)
for k in range(1,N,2): # sum over odd terms
    simp += 4*f(a+k*h)

for k in range(2,N,2): # sum over even terms
    simp += 2*f(a+k*h)

trap = 0.5*f(a) + 0.5*f(b) # Trapezium method
for k in range(1,N):
    trap += f(a+k*h)
    
integralSci = quad(f,a,b)


integralSimp = 1/3 * h * simp
integralTrap = h*trap
print((trueValue / integralSimp )*100)
print(((trueValue / integralTrap))*100)

