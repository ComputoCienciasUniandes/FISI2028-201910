import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("temperatura.dat")

plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.imshow(data)
plt.xlabel("Indice X")
plt.ylabel("Indice T")
plt.colorbar(label="Temperatura")

plt.subplot(1,2,2)
plt.plot(data[0,:], label="tiempo inicial")
plt.plot(data[-1,:], label="tiempo final")
plt.xlabel("Indice X")
plt.ylabel("Temperatura")
plt.legend()
plt.savefig("plot.png", bbox_="tight")
