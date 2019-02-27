import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1

def FD(f, x, h):
    return (f(x+h)-f(x))/h

def CD(f, x, h):
    return (f(x+h/2)-f(x-h/2))/h

def ED(f, x, h):
    return (4*CD(f, x, h/2)-CD(f, x, h))/3.0


def get_error(f, deriva_f_analitica, deriva_f_numerica, x):
    h_range = np.logspace(-15,-1, 200)
    n_points = len(h_range)
    error_range = np.ones(n_points)
    analitica = deriva_f_analitica(x)
    error_range = np.abs((deriva_f_numerica(f, x, h_range) - analitica)/analitica)
    return h_range, error_range


plt.figure(figsize=(15,10))

i = 1
ff = [np.exp, np.sin]
gg = [np.exp, np.cos]
names = ["exp(x)", "sin(x)"]
xx = [0.1, 1.0, 100.0]

for f, g, n, in zip(ff, gg, names):
    for x in xx:
        plt.subplot(2,3,i)

        h, e = get_error(f, g, FD, x); plt.plot(h, e, label="FD")
        h, e = get_error(f, g, CD, x); plt.plot(h, e, label="CD")
        h, e = get_error(f, g, ED, x); plt.plot(h, e, label="ED")

        plt.title("f(x)={}, x={:.1f}".format(n,x))
        plt.xlim([1E-15,1E-1])
        plt.ylim([1E-15,1E-1])
        plt.loglog()
        plt.legend()
        plt.grid()
        plt.xlabel("x")
        plt.ylabel("|error primera derivada|")
        i += 1

plt.savefig("primera_derivada.png", bbox_inches='tight')


# Ejercicio 2


def CD2(f, x, h):
    return (CD(f, x+h/2, h) - CD(f, x-h/2, h))/h

def CD2_bis(f, x, h):
    return (f(x+h) + f(x-h) - 2*f(x))/(h**2)

def minus_cos(x):
    return -np.cos(x)

plt.figure(figsize=(15,10))

i = 1
xx = [0.1, 1.0, 100.0]
for x in xx:
    plt.subplot(2,3,i)
    h, e = get_error(np.cos, minus_cos, CD2, x); plt.plot(h,e, label="CD2")
    h, e = get_error(np.cos, minus_cos, CD2_bis, x); plt.plot(h,e, label="CD2_bis")
    plt.xlim([1E-15,1E-1])
    plt.ylim([1E-15,1E-1])
    plt.loglog()
    plt.legend()
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("|error segunda derivada|")
    plt.title("f(x)=cos(x), x={:.1f}".format(x))
    i += 1

plt.savefig("segunda_derivada.png", bbox_inches='tight')
