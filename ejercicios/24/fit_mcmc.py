import os
import numpy as np
import matplotlib.pyplot as plt

puntos = 30
print('Empezamos! puntos: {}'.format(puntos))
filename = "fit_mcmc.cpp"

#define los nombres de los archivos
execname = filename.split(".")[0]+".x"
dataname = filename.split(".")[0]+".dat"
plotname = filename.split(".")[0]+".png"

# compila
a = os.system("g++ {} -o {}".format(filename, execname))
puntos += 10
print('compilo! puntos: {}'.format(puntos))

# ejecuta
a = os.system("./{} > {}".format(execname, dataname))
puntos += 10
print('ejecuto! puntos: {}'.format(puntos))

# lee los datos observacionales
x = np.loadtxt("valores_x.txt")
y = np.loadtxt("valores_y.txt")

# lee los datos del montecarlo
mcmc_data = np.loadtxt(dataname)
puntos += 10
print('leyo los resultados! puntos: {}'.format(puntos))

#calcula la media de cada columna
params = np.mean(mcmc_data, axis=0)
puntos += 10
print('calculo la media de cada columna! puntos: {}'.format(puntos))

# a partir de esos resultados calcula el fit
def model(x, params):
    y = np.zeros(len(x))
    for i in range(len(params)):
        y = y + (params[i] * x**i)
    return y
x_model = np.linspace(x.min(), x.max(), 100)
y_model = model(x_model, params)
puntos += 10
print('calculo el fit! puntos: {}'.format(puntos))

# prepara la grafica
plt.figure(figsize=(5,5))
plt.errorbar(x, y, yerr=0.1, fmt='o', label='data')
plt.plot(x_model, y_model, label='mcmc fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.savefig(plotname, bbox_inches='tight')
puntos += 10
print('hizo una grafica! puntos: {}'.format(puntos))
print('Si la grafica es algo razonable habra 10 puntos mas')
