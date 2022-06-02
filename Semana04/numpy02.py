import numpy as np
import matplotlib.pyplot as plt
from numpy01 import *

print(2*a1)
print(a1*2)

print(2*a1>10)

print(1/a4 + a4)

plt.plot(a6, a6**2)
plt.show()

plt.hist(a4)
plt.show()

def f(x):
    return x**2 * np.sin(x) / np.exp(-x)

plt.plot(a7, f(a7))
plt.show()