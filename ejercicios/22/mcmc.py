import os
import numpy as np
import matplotlib.pyplot as plt


a = os.system("g++ mcmc.cpp -o mcmc.x")
a = os.system("./mcmc.x > mcmc.dat")

plt.figure()
data = np.loadtxt("mcmc.dat")
plt.hist(data, density=True, bins=40, label='datos')
x = np.linspace(data.min(), data.max(),100)
y = np.exp(-0.5*x*x)/np.sqrt(2.0*np.pi)
plt.plot(x,y, label='resultado esperado')
plt.xlabel('X')
plt.ylabel('Histograma')
plt.legend()
plt.savefig("mcmc.png")
