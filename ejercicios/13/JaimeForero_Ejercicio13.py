import numpy as np

print("")
print("Ejercicio 1.1")
A = np.array([[4, -2, 1, ], [3, 6, -4], [2, 1, 8]])
A_inversa = np.linalg.inv(A)
print("")
print("Matriz A")
print(A)
print("")
print("Matriz A^-1")
print(A_inversa)
print("")
print("Verificando A * A^-1")
print(A@A_inversa)

print("")
print("Ejercicio 1.2")
A_inversa_analitica = (1/263)*np.array([[52, 17, 2],[-32, 30, 19],[-9, -8, 30]])
print("")
print("Cifras significativas en A^{-1}")
print(np.log10(np.abs(A_inversa-A_inversa_analitica)))

print("")
print("Ejercicio 2")
b = np.array([12, -25, 32])
x_sol = np.array([+1, -2, +4])
x = np.linalg.solve(A, b)
print("")
print("numerico: {} . analitico: {}".format(x, x_sol))

b = np.array([+4, -10, +22])
x_sol = np.array([+0.312, -0.038, +2.677])
x = np.linalg.solve(A, b)
print("")
print("numerico: {} . analitico: {}".format(x, x_sol))

b = np.array([+20, -30, +40])
x_sol = np.array([+2.319, -2.965, +4.790])
x = np.linalg.solve(A, b)
print("")
print("numerico: {} . analitico: {}".format(x, x_sol))

print("")
print("Ejercicio 3")
alpha = 2.0
beta = 1.0
A = np.array([[alpha, beta], [-beta, alpha]])
values, vectors = np.linalg.eig(A)
print("")
print('lambda_1 {}. eigenvec_1 {}'.format(values[0], vectors[:,0]))
print('lambda_2 {}. eigenvec_2 {}'.format(values[1], vectors[:,1]))
print('son complejos conjugados como se esperaba')

print("Ejercicio 4")
A = np.array([[-2, +2, -3], [+2, +1, -6], [-1, -2, +0]])
values, vectors = np.linalg.eig(A)
print("")
print("Obtengo autovalores: {}. Esperaba {} {} {}".format(values, 5, -3, -3))
eigen_5 = 1/np.sqrt(6)*np.array([-1, -2, +1])
eigen_3_a = 1/np.sqrt(5)*np.array([-2, +1, 0])
eigen_3_b = 1/np.sqrt(10)*np.array([3, 0, +1])

print("")
print("Eigenvector para lambda=5: {} (que es proporcional a {})".format(vectors[:,1], eigen_5))

print("")
print("Eigenvector para lambda=3: {} ".format(vectors[:,0]))
beta_a = vectors[1,0]*np.sqrt(5) # componente y
beta_b = vectors[2,0]*np.sqrt(10) # componente z
print("Combinacion lineal de dos vectores\n\t vec_a: {} y vec_b {}".format(eigen_3_a, eigen_3_b))
print("\t vec_3 = beta_a * vec_a + beta_b * vec_b: {}".format((beta_a * eigen_3_a + beta_b * eigen_3_b)))

print("")
print("Eigenvector para lambda=3: {} ".format(vectors[:,2]))
beta_a = vectors[1,2]*np.sqrt(5) # componente y
beta_b = vectors[2,2]*np.sqrt(10) # componente z
print("Combinacion lineal de dos vectores\n\t vec_a: {} y vec_b {}".format(eigen_3_a, eigen_3_b))
print("\t vec_3 = beta_a * vec_a + beta_b * vec_b: {}".format((beta_a * eigen_3_a + beta_b * eigen_3_b)))


print("")
print("Ejercicio 5")
n = 100
A = np.zeros([n,n])
b = np.ones(n)
for i in range(1,n+1):
    b[i-1] = 1/i
    for j in range(1,n+1):
        A[i-1,j-1] = 1/(i+j-1)
x = np.linalg.solve(A,b)
print("Solucion con todos los elementos igual a cero salvo el primero:\n\t {}".format(x))
