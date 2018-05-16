# Diffraction limit of a telescope

from scipy import integrate
from math import pi,cos,sin,sqrt
from numpy import empty,array,float,savetxt
from matplotlib import pyplot as plt
a = 0 # lower limit of integration
b = pi # upper limit of integration


    

    
def J(m,x): # Bessel function with f(theta) defined inside to be able to return integral with the factor of 1/pi
    def f(theta):
        return cos(m*theta - x * sin(theta))
    return 1/pi * integrate.quad(f,a,b,limit=80)[0]
    
#def I(l,r):  # intensity of light in diffraction pattern
    #k = 2*pi / l
    #return ((J(1,k*r)) / (k*r))**2
    
besselArray = empty([21,3])

for mIndex in range(0,3):  # using loop to populate array. columns for m=0,1,2 and x in range 1,20
    for xVal in range(0,21):
        besselArray[xVal,mIndex] = J(mIndex,xVal)
 
j0 = besselArray[:,0]  # x and y data
j1 = besselArray[:,1]
j2 = besselArray[:,2]
xList = array(range(0,21))

fig = plt.figure()
plt.plot(xList,j0,label='m = 0')
plt.plot(xList,j1,label = 'm = 1')
plt.plot(xList,j2,label = 'm = 2')
plt.savefig('bessel_5_4.png')




def I(lmda,r): #Intensity
    k = (pi/lmda)    
    return ((J(1,k*r))/(k*r))**2

wavelength = .5        # microm meters
I0 = 1
points = 50          
separation = 0.1 

Intensity = empty([points,points],float)

for i in range(points):
    y = separation*(i - points/2)
    for j in range(points):
        x = separation*(j - points/2)
        r = sqrt((x)**2+(y)**2)

        if r < 0.000000000001:
            Intensity[i,j]= 0.5 #this is the lim as r  -> 0, I -> 0.5
        else: 
            Intensity[i,j] = I0*I(wavelength,r)

#plt.imshow(Intensity,vmax=0.01,cmap='hot')
#plt.gray()
#plt.show()
savetxt('bessel.txt', Intensity)