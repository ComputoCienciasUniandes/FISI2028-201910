import numpy as np
import matplotlib.pyplot as plt

def equilibrio(m, q, l, g):
    def func(theta, A):
        return (np.sin(theta)**3 / np.cos(theta)) - A
    def func_prime(theta, A, h=1E-2):
        return (func(theta+h/2, A) - func(theta-h/2, A))/h
    
    m = m * 1E-3
    q = q * 1E-9
    k = 8.99E9
    A = k*q*q/(4.0*l*l*m*g)
    
    theta = 1E-15
    while np.abs(func(theta, A)) > 1E-15:
        delta_theta = -func(theta, A)/func_prime(theta, A)
        theta += delta_theta
    return theta


def model(x, param):
    '''
    Entrada:
    x: array con valores de entrada para evaluar el modelo.
    param: coeficientes del polinomio param[i] corresponde a x**i
    
    Salida:
    y: array con valores del modelo polinomial evaluado.
    '''
    n_param = len(param)
    y = np.zeros(len(x))
    for i in range(n_param):
        y += param[i] * x**i
    return y 

def matrix_polynomial(filename, poly_degree=2):
    def crea_matriz_modelo_polinomial(x, poly_degree=2):
        n_points = len(x)
        A = np.ones((n_points, poly_degree+1))
        for i in range(poly_degree+1):
            A[:,i] = x**i
        return A
    
    def solve_gauss_jordan(A, b):

        n = len(b)
        for i in range(n): # unos en la diagonal 
            a = A[i,i]
            A[i,:] = A[i,:] / a
            b[i] = b[i]/ a

            for ii in range(i+1,n): # ceros abajo de la diagonal
                a = A[ii,i]
                A[ii,:] = A[ii,:] - a * A[i,:]
                b[ii] = b[ii] - a * b[i]

        # reemplaza hacia arriba
        x = b.copy()
        for i in range(n-1,-1,-1):
            for ii in range(i+1,n):
                x[i] = x[i] - A[i,ii]*x[ii]
        return x
        
    
    datos = np.loadtxt(filename)
    x_obs = datos[:,0]
    y_obs = datos[:,1]
    
    A = crea_matriz_modelo_polinomial(x_obs, poly_degree=poly_degree)
    b = y_obs.copy()
    a = solve_gauss_jordan(A.T @ A, A.T @ b)

    return a

def MCMC_polynomial(filename, poly_degree=2, n_steps=50000):
    def loglikelihood(x_obs, y_obs, sigma_y_obs, param):
        d = y_obs -  model(x_obs, param)
        d = d/sigma_y_obs
        d = -0.5 * np.sum(d**2)
        return d

    def logprior(param):
        return 0.0

    N = n_steps
    datos = np.loadtxt(filename)

    x_obs = datos[:,0]
    y_obs = datos[:,1]
    sigma_y_obs = datos[:,2]

    a = matrix_polynomial(filename, poly_degree=poly_degree) # empiezo en la solucion de minimos cuadrados
    l_param = [a]

    sigma_param = np.ones(poly_degree+1) * np.abs(a) / np.sqrt(N) # dejo un sigma que me permite en principio explorar hasta el origen.
    n_param = len(sigma_param)
    for i in range(1,N):
        propuesta  = l_param[i-1] + np.random.normal(size=n_param) * sigma_param
        logposterior_viejo = loglikelihood(x_obs, y_obs, sigma_y_obs, l_param[i-1]) + logprior(l_param[i-1])
        logposterior_nuevo = loglikelihood(x_obs, y_obs, sigma_y_obs, propuesta) + logprior(propuesta)

        r = min(1,np.exp(logposterior_nuevo-logposterior_viejo))
        alpha = np.random.random()
        if(alpha<r):
            l_param.append(propuesta)
        else:
            l_param.append(l_param[i-1])

    l_param = np.array(l_param)

    # los mejores parametros los tomo como la media.
    a = np.ones(n_param)        
    for i in range(n_param):
        a[i] = np.mean(l_param[:,i])

    return a

