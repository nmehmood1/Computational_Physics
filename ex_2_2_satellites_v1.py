# A program that gives required altitude for desired period of orbit around earth.
# Program then tests 4 different periods and takes the difference between a 24 hour orbit and
# a 23.95 hour sidereal day.

from math import pi
from numpy import array

# Set constants

G = 6.67*10**-11 # Newton's gravitational constant
M = 5.97*10**24 # Mass of Earth
R = 6371*10**3 # Radius of Earth
h2s = 3600 # hours to seconds conversion factor
m2km = 1/1000 # Metres to Kilometres

def altitudeFunc(T): # Returns altitude as a function of Period
    h = ((G*M*T**2)/(4*pi**2))**(1/3) - R
    return h

# Test for 24 hour orbit, 90 minute orbit, 45 minute orbit
periodTest = h2s*array([24,1.5,0.75])
periodList = []
for time in periodTest:
    periodList.append(altitudeFunc(time))

# Find difference between 24 hour orbit and sidereal day, 23.93 Hours

siderealOrbit = altitudeFunc(h2s*23.93)

print("Altitude for 24 hour orbit: " + str(m2km*periodList[0]) + " km")
print("Altitude for 90 minute orbit: " + str(m2km*periodList[1]) + " km")
print("Altitude for 45 minute orbit: " + str(m2km*periodList[2]) + " km")
print("Altitude for 23.95 hour orbit: " + str(m2km*siderealOrbit) + " km")
print("Difference between 24 hour orbit and geosynchronous orbit : " + str((m2km*periodList[0]) - (m2km*siderealOrbit)) + " km")


# Results show the altitudes for geosynchronous orbit and 90 minute orbit at low altitudes. 45 minute orbit is not possible here.
# Next version of program will add classes and allow user to choose different planets in the solar system.

