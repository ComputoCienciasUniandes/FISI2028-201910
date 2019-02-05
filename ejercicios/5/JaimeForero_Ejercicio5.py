# Ejercicios basados en la ssecciones 5.2.2 y 5.2.3 
# del libro A Survey of Computational Physics Introductory Computational Science
# de Landau, Paez, Bordeianu (Python Multimodal eTextBook Beta4.0)

import numpy as np
import matplotlib.pyplot as plt

# Clase que implementa el generador de numeros aleatorios
class MyRandom():
    def __init__(self, seed=1, method="simple"):
        """Inicializacion"""
        self.r  = seed
        if method=="simple":
            self.a = 57
            self.c = 1
            self.M = 265
        elif method=="drand48":
            self.a = int('5DEECE66D', 16)
            self.c = int('B', 16)
            self.M = 2**48
        else:
            print("Error: Metodo no reconocido")
    def random(self):
        """Calcula un nuevo numero aleatorio y actualiza el estado r"""
        r = (self.a * self.r + self.c)%self.M
        self.r = r
        return r/self.M
    
# Genero 1000 puntos con los parametros "malos"
rand = MyRandom(seed=10)
n_points = 1000
r = np.zeros(n_points)
for i in range(n_points):
    r[i] = rand.random()

# Grafica de correlacion
indices = np.arange(n_points)
ii = (indices%2) == 0 # indices pares
plt.figure()
plt.scatter(r[ii], r[~ii])
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("correlacion_simple.png")

# Grafica en funcion del numero de iteracion
indices = np.arange(n_points)
ii = (indices%2) == 0 # indices pares
plt.figure()
plt.plot(r[ii])
plt.xlabel("Numero de secuencia")
plt.ylabel("Numero aleatorio r")
plt.savefig("iteracion_simple.png")

# Genero 1000 puntos con los parametros "buenos"
rand = MyRandom(seed=10, method="drand48")
n_points = 1000
r = np.zeros(n_points)
for i in range(n_points):
    r[i] = rand.random()

# Grafica de correlacion
indices = np.arange(n_points)
ii = (indices%2) == 0 # indices pares
plt.figure()
plt.scatter(r[ii], r[~ii])
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("correlacion_drand48.png")

# Grafica en funcion del numero de iteracion
indices = np.arange(n_points)
ii = (indices%2) == 0 # indices pares
plt.figure()
plt.plot(r[ii])
plt.xlabel("Numero de secuencia")
plt.ylabel("Numero aleatorio r")
plt.savefig("iteracion_drand48.png")


# Verifico la calidad del generador de numeros aleatorios
# comparando el momento 'k'-esimo con su estimacion numerica
# El numero debe ser del orden de uno para considerarlo como 
# un buen generador.

def verifica_momentos(N, k, seed=10, method="simple"):
    rand = MyRandom(seed=seed, method=method)
    r = np.zeros(N)
    for i in range(N):
        r[i] = rand.random()
    d =  np.sqrt(N)*np.abs(np.mean(r**k) - 1.0/(k+1))
    return d

print('Mal generador')
for k in [1,3,7]:
    for N in [1E2, 1E4, 1E5]:
        d= verifica_momentos(int(N), int(k), seed=51, method="simple")
        print('k={}, N={}, d={}'.format(k, N, d))
        
print('Buen generador')
for k in [1,3,7]:
    for N in [1E2, 1E4, 1E5]:
        d= verifica_momentos(int(N), int(k), seed=51, method="drand48")
        print('k={}, N={}, d={}'.format(k, N, d))

