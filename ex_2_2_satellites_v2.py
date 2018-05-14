# A program that gives required altitude for a chosen period and planet.

from math import pi

# Set constants

G = 6.67e-11 # Newton's gravitational constant
h2s = 3600 # hours to seconds conversion factor
m2km = 1/1000 # Metres to Kilometres

#Create planet class

class planet:
    def __init__(self,radius,mass):
        self.r = radius
        self.m = mass
        
mercury = planet(2440e3,3.30e23) # Data for planets
venus = planet(6052e3,4.87e24)
earth = planet(6378e3,5.97e24)
mars = planet(3397e3,6.42e23)
jupiter = planet(71492e3,1.90e27) 
saturn = planet(60268e3,5.68e26)
uranus = planet(25559e3,8.68e25)
neptune = planet(24766e3,1.02e26)

chosenTime = input('Enter period in hours: ') # user input for variables to be used
period = float(chosenTime)*h2s
chosenPlanet = input('Choose a planet: ')


def altitudeFunc(T,aplanet): # Returns altitude as a function of Period
    if chosenPlanet == "mercury":
        h = ((G*mercury.m*T**2)/(4*pi**2))**(1/3) - mercury.r
    elif chosenPlanet == "venus":
        h = ((G*venus.m*T**2)/(4*pi**2))**(1/3) - venus.r
    elif chosenPlanet == "earth":
        h = ((G*earth.m*T**2)/(4*pi**2))**(1/3) - earth.r
    elif chosenPlanet == "mars":
        h = ((G*mars.m*T**2)/(4*pi**2))**(1/3) - mars.r
    elif chosenPlanet == "jupiter":
        h = ((G*jupiter.m*T**2)/(4*pi**2))**(1/3) - jupiter.r
    elif chosenPlanet == "saturn":
        h = ((G*saturn.m*T**2)/(4*pi**2))**(1/3) - saturn.r
    elif chosenPlanet == "uranus":
        h = ((G*uranus.m*T**2)/(4*pi**2))**(1/3) - uranus.r
    elif chosenPlanet == "neptune":
        h = ((G*neptune.m*T**2)/(4*pi**2))**(1/3) - neptune.r
    else:
        print("Please enter a valid planet")
    return round(h*m2km,3)

print("Required altitude for orbital period of " + str(chosenTime) + " hours around \
" + str(chosenPlanet) + " is " + str((altitudeFunc(period,chosenPlanet))) + " km.")

#In next version of program, I will import planet data from csv file
