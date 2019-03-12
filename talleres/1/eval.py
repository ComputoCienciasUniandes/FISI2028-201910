filename = "JaimeForero_Taller1"
print("Calificando {}".format(filename))
sol = __import__(filename)

import numpy as np

ans_theta = 0.028411307356677486
ans_a = np.array([  1.26264805,  -7.9664384,   27.30330289, -21.31548334])
ans_b = np.array([ 9.90862659e-01, 1.37325245e-01, -3.13890413e+01, 1.48506447e+02, -2.13289880e+02, 9.68677065e+01]) 

total = 0

# primer punto
puntos=5
try:
    theta = sol.equilibrio(1E-2, 1.0, 1.0, 9.8)
    puntos +=5
    try:
        np.testing.assert_allclose(theta, ans_theta, rtol=1E-4)
        puntos +=10
    except:
        puntos +=0 
except:
    puntos += 0
print('primer punto', puntos)
total += puntos

puntos=10
# Segundo punto
try:
    a = sol.matrix_polynomial("numeros.txt", poly_degree=3)
    b = sol.matrix_polynomial("numeros.txt", poly_degree=5)
    puntos += 10
    try:
        ll = np.testing.assert_allclose(a, ans_a, rtol=1E-4)
        puntos += 5
    except:
        puntos += 0

    try:
        np.testing.assert_allclose(b, ans_b, rtol=1E-4)
        puntos += 5
    except:
        puntos += 0
except:
    puntos += 0
print('segundo punto', puntos)
total += puntos

puntos=15
try:
    a = sol.MCMC_polynomial("numeros.txt", poly_degree=3, N=60000)
    b = sol.MCMC_polynomial("numeros.txt", poly_degree=5, N=60000)
    puntos += 15
    try:

        np.testing.assert_allclose(a, ans_a, rtol=1) 
        puntos += 10
    except:
        puntos += 0

    try:
        np.testing.assert_allclose(b, ans_b, rtol=1) 
        puntos += 10
    except:
        puntos += 0
except:
    puntos += 0
print('tercer punto', puntos)# Segundo punto
total += puntos

print('total', total)




