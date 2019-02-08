import numpy as np
import matplotlib.pyplot as plt


def walk(n_steps=1000, dim=2):
    """Hace una marcha aleatoria"""
    delta_x = 2.0*np.random.random(n_steps) - 1.0
    delta_y = 2.0*np.random.random(n_steps) - 1.0
    if dim==3:
        delta_z = 2.0*np.random.random(n_steps) - 1.0
    else:
        delta_z = np.zeros(n_steps)
    L = np.sqrt(delta_x**2 + delta_y**2 + delta_z**2)
    delta_x = delta_x/L
    delta_y = delta_y/L
    delta_z = delta_z/L
    x = np.cumsum(delta_x)
    y = np.cumsum(delta_y)
    z = np.cumsum(delta_z)
    R2 = x[-1]**2 + y[-1]**2 + z[-1]**2 
    return {'x':x, 'y':y, 'z':z, 'delta_x':delta_x, 'delta_y':delta_y, 'delta_z':delta_z, 'R2':R2}

def ensemble(n_steps=1000, dim=2):
    """Crea un conjunto de marchas aleatorias"""
    K = int(np.sqrt(n_steps))
    e = {}
    for k in range(K):
        e[k] = walk(n_steps=n_steps, dim=dim)
    return e

def average_ensemble(E):
    """Calcula el promedio de R2 sobre un ensemble de marchas"""
    r2 = np.zeros(len(E))
    for k in E.keys():
        r2[k] = E[k]['R2']
    return np.mean(r2)

print('-------------')
print('Marchas en 2D')
print('-------------')

# Crea un ensemble de marchas aleatorias 2D
E = ensemble(n_steps=1000, dim=2)

# Hace la grafica de las marchas
plt.figure()
for k in E.keys():
    plt.plot(E[k]['x'], E[k]['y'], color='black', alpha=0.4)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ensemble de {:d} marchas aleatorias'.format(len(E)))
plt.savefig('ensemble_2D.png')


# Calcula <R2> para el ensemble de marchas aleatorias
R2_ensemble = np.zeros(len(E))
for k in E.keys():
    R2_ensemble[k] = E[k]['R2'] 
print('R2 promedio: {:.2f}. (Deberia ser cercano a {:d})'.format(R2_ensemble.mean(), len(E[0]['x'])))


# Calculo D = <delta_x_i * delta_x_j>/R2 + <delta_y_i * delta_y_j>/R2 para una sola marcha

one_walk = E[0]
n_points = len(one_walk['x'])

D = (np.sum(one_walk['delta_x']))**2 + (np.sum(one_walk['delta_y']))**2 + (np.sum(one_walk['delta_z']))**2
D = D-np.sum(one_walk['delta_x']**2 + one_walk['delta_y']**2 + one_walk['delta_z']**2)
D = D/one_walk['R2']
print('Suma de los terminos [(delta_x_i * delta_x_j) + (delta_y_i * delta_y_j)]/R2: {:.3f}'.format(D))


# Calculo D = <delta_x_i * delta_x_j>/R2 + <delta_y_i * delta_y_j>/R2 para todas las marchas y doy el promedio

D = np.zeros(len(E))
R2 = np.zeros(len(E))
for k in range(len(E)):
    one_walk = E[k]
    D[k] = (np.sum(one_walk['delta_x']))**2 + (np.sum(one_walk['delta_y']))**2 + (np.sum(one_walk['delta_z']))**2
    D[k] = D[k]-np.sum(one_walk['delta_x']**2 + one_walk['delta_y']**2 + one_walk['delta_z']**2)
    D[k] = D[k]/one_walk['R2']
print('Promedio de los terminos [(delta_x_i * delta_x_j) + (delta_y_i * delta_y_j)]/R2: {:.3f}'.format(np.mean(D)))

# Ensembles para diferentes valores de N
N_list = [10, 100, 500, 1000, 5000, 10000, 20000, 100000]
R2 = np.zeros(len(N_list))
for i in range(len(N_list)):
    E = ensemble(n_steps=N_list[i], dim=2)
    R2[i] = average_ensemble(E)

# R2 en funcion de N

plt.figure()
plt.plot(N_list, R2, label='Experimento')
plt.plot(N_list, N_list, label='Teoria')
plt.loglog()
plt.legend()
plt.title('Marchas Aleatorias en 2D')
plt.xlabel("N_steps")
plt.ylabel("<$R^2$>")
plt.savefig('comparacion_N_R2_2D.png')



print('-------------')
print('Marchas en 3D')
print('-------------')

# Crea un ensemble de marchas aleatorias 2D
E = ensemble(n_steps=1000, dim=3)

# Hace la grafica de las marchas
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
for k in E.keys():
    plt.plot(E[k]['x'], E[k]['y'], color='black', alpha=0.4)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ensemble de {:d} marchas aleatorias'.format(len(E)))

plt.subplot(1,3,2)
for k in E.keys():
    plt.plot(E[k]['y'], E[k]['z'], color='black', alpha=0.4)
plt.xlabel('Y')
plt.ylabel('Z')
plt.title('Ensemble de {:d} marchas aleatorias'.format(len(E)))

plt.subplot(1,3,3)
for k in E.keys():
    plt.plot(E[k]['x'], E[k]['z'], color='black', alpha=0.4)
plt.xlabel('X')
plt.ylabel('Z')
plt.title('Ensemble de {:d} marchas aleatorias'.format(len(E)))

plt.savefig('ensemble_3D.png')


# Calcula <R2> para el ensemble de marchas aleatorias
R2_ensemble = np.zeros(len(E))
for k in E.keys():
    R2_ensemble[k] = E[k]['R2'] 
print('R2 promedio: {:.2f}. (Deberia ser cercano a {:d})'.format(R2_ensemble.mean(), len(E[0]['x'])))


# Calculo D = <delta_x_i * delta_x_j>/R2 + <delta_y_i * delta_y_j>/R2 para una sola marcha

one_walk = E[0]
n_points = len(one_walk['x'])

D = (np.sum(one_walk['delta_x']))**2 + (np.sum(one_walk['delta_y']))**2 + (np.sum(one_walk['delta_z']))**2
D = D-np.sum(one_walk['delta_x']**2 + one_walk['delta_y']**2 + one_walk['delta_z']**2)
D = D/one_walk['R2']
print('Suma de los terminos [(delta_x_i * delta_x_j) + (delta_y_i * delta_y_j)]/R2: {:.3f}'.format(D))


# Calculo D = <delta_x_i * delta_x_j>/R2 + <delta_y_i * delta_y_j>/R2 para todas las marchas y doy el promedio

D = np.zeros(len(E))
R2 = np.zeros(len(E))
for k in range(len(E)):
    one_walk = E[k]
    D[k] = (np.sum(one_walk['delta_x']))**2 + (np.sum(one_walk['delta_y']))**2 + (np.sum(one_walk['delta_z']))**2
    D[k] = D[k]-np.sum(one_walk['delta_x']**2 + one_walk['delta_y']**2 + one_walk['delta_z']**2)
    D[k] = D[k]/one_walk['R2']
print('Promedio de los terminos [(delta_x_i * delta_x_j) + (delta_y_i * delta_y_j)]/R2: {:.3f}'.format(np.mean(D)))

# Ensembles para diferentes valores de N
N_list = [10, 100, 500, 1000, 5000, 10000, 20000, 100000]
R2 = np.zeros(len(N_list))
for i in range(len(N_list)):
    E = ensemble(n_steps=N_list[i], dim=3)
    R2[i] = average_ensemble(E)

# R2 en funcion de N

plt.figure()
plt.plot(N_list, R2, label='Experimento')
plt.plot(N_list, N_list, label='Teoria')
plt.loglog()
plt.legend()
plt.title('Marchas Aleatorias en 3D')
plt.xlabel("N_steps")
plt.ylabel("<$R^2$>")
plt.savefig('comparacion_N_R2_3D.png')
