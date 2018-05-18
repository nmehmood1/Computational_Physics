from math import exp
x = 1.0
for k in range(10):
    x = 2 - exp(-x)
    print(x)