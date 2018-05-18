# # solving simultaneous equations using matrices
# circuit of resistors
# write equations for four junctions with unknown voltages

import numpy as np

V_0 = 5

A = np.array([[4,-1,-1,-1],
              [-1,3,0,-1],
              [-1,0,3,-2],
              [-1,-1,-1,4]])

v = np.array([[V_0],
              [0],
              [V_0],
              [0]])
              
x = np.linalg.solve(A,v)

