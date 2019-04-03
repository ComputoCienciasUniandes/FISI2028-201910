# Corresponde a la implementacion en python de algunos algoritmos 
# en el primer capitulo de Algorithms and Computations de Werner Krauth.

import numpy as np

def direct_pi(N):
    N_hits = 0 
    for i in range(N):
        x = 2.0*(np.random.random()-0.5)
        y = 2.0*(np.random.random()-0.5)
        if(x**2 + y**2 < 1):
            N_hits += 1
    return N_hits

print('direct_pi(1000)',direct_pi(1000))


def markov_pi(N):
    N_hits = 0
    x = 1.0
    y = 1.0
    delta = 0.1
    for i in range(N):
        delta_x = delta * 2.0 * (np.random.random()-0.5)
        delta_y = delta * 2.0 * (np.random.random()-0.5)
        if(abs(x+delta_x)<1 and abs(y+delta_y)<1):
            x += delta_x
            y += delta_y
        if (x**2 + y**2 < 1):
            N_hits += 1
    return N_hits

print('markov_pi(1000):', markov_pi(1000))


def markov_two_site(k, p_0=0.1, p_1=0.9):
    def proba(m):
        if(m==0): a = 0.5
        if(m==1): a = 0.5
        return a

    if(k==0): l=1
    if(k==1): l=0
    
    gamma = proba(l)/proba(k)
    r = np.random.random()
    if r < gamma:
        k = l
    return k

print('markov_two_site:')
k = 0
for i in range(10):
    k = markov_two_site(k)
    print(k)


def reject_continous():
    def proba_dens(x):
        """Corresponde a exp(-x) entre 0 y 1.
        """
        norm = 1.0 - np.exp(-1)
        return norm * np.exp(-x)
    p_max = proba_dens(0)

    x_rand = np.random.random()
    gamma = np.random.random() * p_max
    while gamma > proba_dens(x_rand) :
            x_rand = np.random.random()
            gamma = np.random.random() * p_max
    return x_rand

print('reject_continous')
for i in range(10):
    print(reject_continous())
    
def gauss(sigma):
    phi = np.random.random() * 2.0 * np.pi
    gamma = -np.log(np.random.random())
    r = sigma * np.sqrt(2.0 * gamma)
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return x, y

print('gauss')
for i in range(10):
    print(gauss(1.0))
