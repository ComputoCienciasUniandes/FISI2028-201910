import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("placas.dat")
n_points = int(np.sqrt(len(data)))
grid = np.reshape(data, (n_points, n_points))
print(n_points)


plt.figure()
plt.imshow(grid)
plt.xlabel("X")
plt.ylabel("Y")
plt.colorbar(label="Potencial")
plt.savefig("plot.png")
