import os
import numpy as np
import matplotlib.pyplot as plt


filename = "fit_mcmc.cpp"

#define los nombres de los archivos
execname = filename.split(".")[0]+".x"
dataname = filename.split(".")[0]+".dat"
plotname = filename.split(".")[0]+".png"

# compila
a = os.system("g++ {} -o {}".format(filename, execname))

# ejecuta
a = os.system("./{} > {}".format(execname, dataname))

# lee los datos observacionales
x = np.loadtxt("valores_x.txt")
y = np.loadtxt("valores_y.txt")

# lee los datos del montecarlo
mcmc_data = np.loadtxt(dataname)

#calcula la media de cada columna
params = np.mean(mcmc_data, axis=0)

# a partir de esos resultados calcula el fit
def model(x, params):
    y = np.zeros(len(x))
    for i in range(len(params)):
        y = y + (params[i] * x**i)
    return y
x_model = np.linspace(x.min(), x.max(), 100)
y_model = model(x_model, params)

# prepara la grafica
plt.figure(figsize=(5,5))
plt.errorbar(x, y, yerr=0.1, fmt='o', label='data')
plt.plot(x_model, y_model, label='mcmc fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.savefig(plotname, bbox_inches='tight')
