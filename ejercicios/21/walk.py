import os
import numpy as np
import matplotlib.pyplot as plt


os.system("g++ walk.cpp -o walk.x")
os.system("./walk.x > walk.dat")

plt.figure()
data = np.loadtxt("walk.dat")
plt.plot(data[:,0], data[:,1])
plt.axis('square')
plt.xlim([-25, 25])
plt.ylim([-25, 25])
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("walk.png")
