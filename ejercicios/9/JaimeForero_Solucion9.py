import numpy as np
import matplotlib.pyplot as plt

# Primera parte

# Soluciones a los ejercicios de la seccion 6.2.5 
# del libro A Survey of Computational Physics Introductory Computational Science
# de Landau, Paez, Bordeianu (Python Multimodal eTextBook Beta4.0)

#1. Write a double-precision program to integrate an arbitrary function numerically 
# using the trapezoid rule, the Simpson rule, and Gaussian quadrature.
def integra(f, a, b, n_points=10, metodo="trapecio"):
    # Genera siempre un numero impar de puntos
    if n_points%2 == 0:
        n_points = n_points + 1

    if metodo=="trapecio":
        x = np.linspace(a, b, n_points)
        h = x[1] - x[0]
        w = np.ones(n_points) * h
        w[0] = h/2
        w[-1] = h/2
    elif metodo=="simpson":
        x = np.linspace(a, b, n_points)
        h = x[1] - x[0]
        w = np.ones(n_points) 
        ii = np.arange(n_points)
        w[ii%2!=0] = 4.0*h/3.0
        w[ii%2==0] = 2.0*h/3.0
        w[0] = h/3
        w[-1] = h/3
    elif metodo=="cuadratura":
        y, wprime = np.polynomial.legendre.leggauss(n_points)
        x = 0.5*(b+a) + 0.5*(b-a)*y
        w = 0.5*(b-a)*wprime
    else:
        print('metodo no implementado')
        x = np.zeros(n_points)
        y = np.zeros(n_points)

    return np.sum(f(x)*w)

def func(x):
    return np.sin(x)

def error(x):
    return np.abs(2-x)/2

# 2 Compute the relative error (epsilon=abs(numerical-exact)/exact) in each case. 
# Present your data in tabular form for N=2,10,20,40,80,160

N = [2,10,20,40,80,160]
print("Primera Parte")
out = open("tabla_resultados.dat", "w")
print("# N\t e_T\t e_S \t e_G")
for n_points in N:
    a = integra(func, 0, np.pi, n_points=n_points, metodo="trapecio")
    b = integra(func, 0, np.pi, n_points=n_points, metodo="simpson")
    c = integra(func, 0, np.pi, n_points=n_points, metodo="cuadratura")
    print("{:d}\t {:.1e} {:.1e} {:.1e}".format(n_points, error(a), error(b), error(c)))
    out.write("{:d}\t {:.1e} {:.1e} {:.1e}\n".format(n_points, error(a), error(b), error(c)))
out.close()
print("")

# 3 Make a log-log plot of relative error versus N
data = np.loadtxt("tabla_resultados.dat")
plt.figure()
plt.plot(data[:,0], data[:,1], label="Trapecio")
plt.plot(data[:,0], data[:,2], label="Simpson")
plt.plot(data[:,0], data[:,3], label="Cuadratura")

plt.xlabel('N')
plt.ylabel('|error|')
plt.loglog()
plt.legend()
plt.savefig("loglogplot.png")


# 4. Use your plot or table to estimate the power-law dependence of the error on N and
# to determine the nuber of decimal places of precision.

for i,m in zip([1,2,3],["Trapecio", "Simpson", "Cuadratura"]):
    power_law = (np.log(data[2,i]) - np.log(data[0,i]))/(np.log(data[2,0]) - np.log(data[0,0]))
    decimal_places = -np.log10(data[-1,i])
    print("Metodo {}".format(m))    
    print("\t Power Law: {:.1f}".format(power_law))
    print("\t Decimal Places: {:d}".format(int(decimal_places)))

print("")

# Segunda parte.
# Calcule la integral de la función Gamma (https://en.wikipedia.org/wiki/Gamma_function) para z>1. Imprima los resultados Gamma(2), Gamma(3) y Gamma(4). 

def gamma(z, n_points=20):
    def fun(z, x):
        return x**(z-1) * np.exp(-x)
    # Usando la formula de transformacion (6.36) del libro.
    y, wprime = np.polynomial.legendre.leggauss(n_points)
    x = (1+y)/(1-y)
    w = wprime * 2/(1-y)**2
    return np.sum(fun(z,x)*w)
print("Segunda Parte")
print("Gamma(2): {}\nGamma(3): {}\nGamma(4): {}\t".format(gamma(2), gamma(3), gamma(4)))


def gamma2(z, n_points=20):
    # Usando el cambio de variable u = exp(-x)
    def fun(z,u):
        return (-np.log(u))**(z-1)    # diverge para u=0
    a = 0.0
    b = 1.0
    y, wprime = np.polynomial.legendre.leggauss(n_points)
    x = 0.5*(b+a) + 0.5*(b-a)*y
    w = 0.5*(b-a)*wprime
    return np.sum(fun(z,x)*w)
print("Segunda Parte")
print("Gamma(2): {}\nGamma(3): {}\nGamma(4): {}\t".format(gamma2(2), gamma2(3), gamma2(4)))

