import numpy as np
import matplotlib.pyplot as plt

def crea_matriz_modelo_polinomial(x, poly_deg=2):
    n_points = len(x)
    A = np.ones((n_points, poly_deg+1))
    for i in range(poly_deg+1):
        A[:,i] = x**i
    return A

def poly_model(x, c):
    n = len(c)
    y = np.zeros(len(x))
    for i in range(n):
        y += c[i] * x**i
    return y
    

# Ejercicio 1
data = np.loadtxt("numeros_6.txt")
x = data[:,0]
y = data[:,1]

# Resuelve el sistema lineal 
A = crea_matriz_modelo_polinomial(x, poly_deg=len(x)-1)
A_inv = np.linalg.inv(A) # saco la inversa de A
c = A_inv@y


# datos del modelo
x_model = np.linspace(x.min(), x.max(), 100)
y_model = poly_model(x_model, c)

# grafica
plt.figure()
plt.plot(x_model, y_model, label='fit')
plt.scatter(x, y, label='data')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("fit_parte_1.png")


# Ejercicio 2 
data = np.loadtxt("numeros_20.txt")
x = data[:,0]
y = data[:,1]

# Resuelve el sistema lineal, guarda los coeficients en un diccionario
# para los ajustes de polinomios de orden 0, 1, 2.
c = {}
for n in [0,1,2]:
    A = crea_matriz_modelo_polinomial(x, poly_deg=n)
    A_inv = np.linalg.pinv(A) # esta ves uso la pseudo inversa
    c[n] = A_inv@y

# datos del modelo
x_model = np.linspace(x.min(), x.max(), 100)

# grafica
plt.figure()
for n in [0, 1, 2]:
    y_model = poly_model(x_model, c[n])
    plt.plot(x_model, y_model, label='fit orden {}'.format(n))

plt.scatter(x, y, label='data', color='black')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("fit_parte_2.png")
