# This will plot the first 1000 months after january 1749 and the number of sunspots detected that month. It also plots the running average.

import numpy as np 
import matplotlib.pyplot as plt
r = 5
#plot first 1000 data points of sunspot count vs month

sunspots = np.loadtxt("sunspots.txt",float)
xData = sunspots[:,0]
yData = sunspots[:,1]

plt.plot(xData,yData)
plt.xlabel('Months Since Jan 1749')
plt.ylabel('Number of Sunspots')
plt.xlim(0,1000)

#plot running average on same graph
runSum = np.cumsum(yData) # I have chosen to produce an array using cumsum and 
#                           divide elementwise with a numberline array
numLine = np.arange(1,3144)
runAvg = (np.divide(runSum,numLine))

plt.plot(xData,runAvg,label = 'Running Avg.')
plt.xlim(0,1000)
plt.legend()
plt.savefig('ex3.1.png')
