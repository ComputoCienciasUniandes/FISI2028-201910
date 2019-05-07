import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


data = np.loadtxt("onda.dat")
print(np.shape(data))
x = np.linspace(0.0, 1.0, np.shape(data)[1])
t = np.linspace(0.0, 6.0, np.shape(data)[0])
X, T = np.meshgrid(x,t)

fig = plt.figure(figsize=(13,5))
ax = fig.add_subplot(121, projection="3d")
surf = ax.plot_surface(X, T, data, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.xlabel("Posicion [metros[]")
plt.ylabel("Tiempo [segundos]")
ax.set_zlim3d(-1, 1)
ax.view_init(20, 20)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.subplot(1,2,2)
plt.plot(x, data[0,:], label="tiempo inicial")
plt.plot(x, data[-1,:], label="tiempo final")
plt.xlabel("Posicion [metros]")
plt.ylabel("Desplazamiento [metros]")
plt.legend()
plt.savefig("plot.png", bbox_inches="tight")
