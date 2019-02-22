import numpy as np
import matplotlib.pyplot as plt

# Primera parte

def integral(dim=10, n_points=100):
    x = np.random.random((dim, n_points))
    x_sum = np.sum(x, axis=0)
    x_sum = np.average(x_sum**2)
    return x_sum

def integral(dim=10, n_points=100):
    suma = 0.0
    for i in range(n_points):
        x =  np.random.random(dim)
        suma += np.sum(x*x)
    return suma/n_points

def mean_integral(n_trial=16, dim=10, n_points=100):
    x = 0
    for i in range(n_trial):
        x +=  integral(dim=dim, n_points=n_points)
    x = x/n_trial
    return x


N = 2**np.arange(1,14)
error = []
for n in N:
    error.append(np.abs(155/6-mean_integral(n_points=n))/(155/6))

plt.figure()
plt.plot(1/np.sqrt(N), error)
plt.loglog()
plt.title("$\int_0^{1} dx_1 \ldots \int_0^1 dx_{10} (x_1+\cdots x_{10})^2 $")
plt.ylabel("|error|")
plt.xlabel("1/$\sqrt{N}$")
plt.savefig("error_1.png")

# Segunda parte

#10.1
def f(x):
    return np.sin(x)

def integral_analitica():
    return np.cos(0) - np.cos(1.0)

def integral_monte_carlo(N=100):
    x = np.random.random(N)
    return np.sum(f(x))/N

n_intentos = 10
puntos = np.int_(np.logspace(1,5,n_intentos))
diferencias = np.ones(n_intentos)
for i in range(n_intentos):
    a = integral_analitica()
    b = integral_monte_carlo(N=puntos[i])
    diferencias[i] =  (np.abs((a-b)/a))
    
plt.figure()
plt.plot(puntos, diferencias)
plt.loglog()
plt.title("$\int_0^{1} sin(x) dx$")
plt.xlabel("$N_{puntos}$")
plt.ylabel("|Error|")
plt.savefig("error_2.png")


# 10.2

def f(x):
    return np.sin(x)

def integral_analitica():
    return 1.0

def integral_monte_carlo(N=100):
    x = np.sqrt(np.random.random(N))*np.pi/2.0
    norm = np.pi**2/8
    return norm * np.average(f(x))

n_intentos = 10
puntos = np.int_(np.logspace(1,5,n_intentos))
diferencias = np.ones(n_intentos)
for i in range(n_intentos):
    a = integral_analitica()
    b = integral_monte_carlo(N=puntos[i])
    diferencias[i] =  (np.abs((a-b)/a))
    
plt.figure()
plt.plot(puntos, diferencias)
plt.loglog()
plt.title("$\int_0^{\pi/2} x\sin(x) dx$")
plt.xlabel("$N_{puntos}$")
plt.ylabel("|Error|")
plt.savefig("error_3.png")
