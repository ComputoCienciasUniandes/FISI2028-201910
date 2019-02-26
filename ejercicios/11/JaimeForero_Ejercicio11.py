import numpy as np
import matplotlib.pyplot as plt

def FD(f, x, h):
    return (f(x+h)-f(x))/h

def CD(f, x, h):
    return (f(x+h/2)-f(x-h/2))/h

def ED(f, x, h):
    return (4*CD(f, x, h/2)-CD(f, x, h))/3.0


def get_error(f, deriva_f_analitica, deriva_f_numerica, x):
    h_range = np.logspace(-15,-1, 100)
    n_points = len(h_range)
    error_range = np.ones(n_points)
    for i in range(n_points):
        h = h_range[i]
        analitica = deriva_f_analitica(x)
        error_range[i] = np.abs((deriva_f_numerica(f, x, h) - analitica)/analitica)
    return h_range, error_range


plt.figure(figsize=(15,10))

i = 1
xx = [0.1, 1.0, 100.0]
for x in xx:
    plt.subplot(2,3,i)
    h, e = get_error(np.exp, np.exp, FD, x); plt.plot(h,e, label="FD")
    h, e = get_error(np.exp, np.exp, CD, x); plt.plot(h,e, label="CD")
    h, e = get_error(np.exp, np.exp, ED, x); plt.plot(h,e, label="ED")
    plt.xlim([1E-15,1E-1])
    plt.ylim([1E-15,1])
    plt.loglog()
    plt.legend()
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("|error|")
    plt.title("f(x)=exp(x), x={:.1f}".format(x))
    i += 1


i = 4
xx = [0.1, 1.0, 100.0]
for x in xx:
    plt.subplot(2,3,i)
    h, e = get_error(np.sin, np.cos, FD, x); plt.plot(h,e, label="FD")
    h, e = get_error(np.sin, np.cos, CD, x); plt.plot(h,e, label="CD")
    h, e = get_error(np.sin, np.cos, ED, x); plt.plot(h,e, label="ED")
    plt.xlim([1E-15,1E-1])
    plt.ylim([1E-15,1])
    plt.loglog()
    plt.legend()
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("|error|")
    plt.title("f(x)=sin(x), x={:.1f}".format(x))
    i += 1

plt.savefig("primera_derivada.png")
