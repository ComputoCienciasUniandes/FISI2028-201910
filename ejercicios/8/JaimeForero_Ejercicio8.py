import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 7.1

def f(x):
    y = 0.5 * np.sin(x)
    if(np.isscalar(x)):# esto va a funcionar si entra un numero
        if (x>np.pi) | (x<0):
            y = 0
    else: #esto va a funcionar si entra un array
        ii = (x>np.pi) | (x<0)
        y[ii] = 0.0
    return y

def metropolis(N=100000, sigma_delta=1.0):
    lista = [np.random.random()*np.pi]

    for i in range(1,N):
        propuesta  = lista[i-1] + np.random.normal(loc=0.0, scale=sigma_delta)
        r = min(1,f(propuesta)/f(lista[i-1]))
        alpha = np.random.random()
        if(alpha<r):
            lista.append(propuesta)
        else:
            lista.append(lista[i-1])
    return np.array(lista)


lista_a = metropolis()
lista_b = metropolis(sigma_delta=1E-3)
lista_c = metropolis(sigma_delta=1E3)

x = np.linspace(0, np.pi, 100)
y = f(x)

plt.figure()

plt.plot(x, f(x), label='Funcion Analitica')
_ = plt.hist(lista_a, density=True, label='$\sigma_{\delta}=1$', bins=x)
_ = plt.hist(lista_b, density=True, label='$\sigma_{\delta}=10^{-3}$', bins=x)
_ = plt.hist(lista_c, density=True, label='$\sigma_{\delta}=10^{3}$', bins=x)
plt.xlabel('x')
plt.ylabel('PDF(x)')
plt.legend()
plt.savefig('metropolis_delta.png')


# Ejercicio 7.2
def dens(x, y):
    return np.exp(-0.5*(x**2/4 + y**2 +x*y/1.5))
    
def metropolis_2D(N=100000, sigma_delta=0.5):

    lista_x = [np.random.random()]
    lista_y = [np.random.random()]

    for i in range(1,N):
        propuesta_x  = lista_x[i-1] + np.random.normal(loc=0.0, scale=sigma_delta)
        propuesta_y  = lista_y[i-1] + np.random.normal(loc=0.0, scale=sigma_delta)

        r = min(1, dens(propuesta_x, propuesta_y)/dens(lista_x[i-1], lista_y[i-1]))
        alpha = np.random.random()
        if(alpha<r):
            lista_x.append(propuesta_x)
            lista_y.append(propuesta_y)
        else:
            lista_x.append(lista_x[i-1])
            lista_y.append(lista_y[i-1])
    return np.array(lista_x), np.array(lista_y)


# Genera puntos sobre una grid
x_line = np.linspace(-5,5,100)
y_line = np.linspace(-5,5,100)
x_grid, y_grid = np.meshgrid(x_line, y_line)
z_grid = dens(x_grid, y_grid)

# Genera lista de puntos
x_lista, y_lista =  metropolis_2D()

plt.subplot(1,2,1)
# grafica los puntos de la grid
im = plt.pcolormesh(x_grid, y_grid, z_grid)
plt.title('Analitico')

# grafica el histograma bidimensional a partir de la lista de puntos
plt.subplot(1,2,2)

_ = plt.hist2d(x_lista, y_lista, bins=50)
plt.title('Monte Carlo')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.savefig('metropolis_2D.png')

# Ejercicio 8.1

x_obs = np.array([-2.0,1.3,0.4,5.0,0.1, -4.7, 3.0, -3.5,-1.1])
y_obs = np.array([ -1.931,   2.38,   1.88,  -24.22,   3.31, -21.9,  -5.18, -12.23,   0.822])
sigma_y_obs = ([ 2.63,  6.23, -1.461, 1.376, -4.72,  1.313, -4.886, -1.091,  0.8054])

def model(x,a,b,c):
    return a*x**2 + b*x + c

# Numericamente es mas estable trabajar con el logaritmo
def loglikelihood(x_obs, y_obs, sigma_y_obs, a, b, c):
    d = y_obs -  model(x_obs, a, b, c)
    d = d/sigma_y_obs
    d = -0.5 * np.sum(d**2)
    return d

# Numericamente es mas estable trabajar con el logaritmo
def logprior(a, b, c):
    p = -np.inf
    if a < 20 and a >-20 and b >-20 and b<20 and c <20 and c>-20:
        p = 0.0
    return p

N = 50000
lista_a = [np.random.random()]
lista_b = [np.random.random()]
lista_c = [np.random.random()]

logposterior = [loglikelihood(x_obs, y_obs, sigma_y_obs, lista_a[0], lista_b[0], lista_c[0]) + logprior(lista_a[0], lista_b[0], lista_c[0])]

sigma_delta_a = 0.2
sigma_delta_b = 0.2
sigma_delta_c = 0.2

for i in range(1,N):
    propuesta_a  = lista_a[i-1] + np.random.normal(loc=0.0, scale=sigma_delta_a)
    propuesta_b  = lista_b[i-1] + np.random.normal(loc=0.0, scale=sigma_delta_b)
    propuesta_c  = lista_c[i-1] + np.random.normal(loc=0.0, scale=sigma_delta_c)

    logposterior_viejo = loglikelihood(x_obs, y_obs, sigma_y_obs, lista_a[i-1], lista_b[i-1], lista_c[i-1]) + logprior(lista_a[i-1], lista_b[i-1], lista_c[i-1])
    logposterior_nuevo = loglikelihood(x_obs, y_obs, sigma_y_obs, propuesta_a, propuesta_b, propuesta_c) + logprior(propuesta_a, propuesta_b, propuesta_c)

    r = min(1,np.exp(logposterior_nuevo-logposterior_viejo))
    alpha = np.random.random()
    if(alpha<r):
        lista_a.append(propuesta_a)
        lista_b.append(propuesta_b)
        lista_c.append(propuesta_c)
        logposterior.append(logposterior_nuevo)
    else:
        lista_a.append(lista_a[i-1])
        lista_b.append(lista_b[i-1])
        lista_c.append(lista_c[i-1])
        logposterior.append(logposterior_viejo)
lista_a = np.array(lista_a[1000:])
lista_b = np.array(lista_b[1000:])
lista_c = np.array(lista_c[1000:])

plt.figure(figsize=(7,7))

plt.subplot(2,2,1)
x_model = np.linspace(x_obs.min(), x_obs.max(), 100)
y_model = model(x_model, np.mean(lista_a), np.mean(lista_b), np.mean(lista_c))
plt.errorbar(x_obs,y_obs, yerr=sigma_y_obs, fmt='o', label='observaciones')
plt.plot(x_model, y_model, label='modelo')
plt.legend()

plt.subplot(2,2,2)
_=plt.hist(lista_a, bins=40, density=True)
plt.xlabel('a')
plt.ylabel('P(a|datos)')

plt.subplot(2,2,3)
_=plt.hist(lista_b, bins=40, density=True)
plt.xlabel('b')
plt.ylabel('P(b|datos)')

plt.subplot(2,2,4)
_=plt.hist(lista_c, bins=40, density=True)
plt.xlabel('c')
plt.ylabel('P(c|datos)')

plt.savefig('modelo_cuadratico.png')
