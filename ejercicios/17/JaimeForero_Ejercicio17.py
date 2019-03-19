import numpy as np
import matplotlib.pyplot as plt

def FT(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        X[k] = 0.0j
        for n in range(N):
            X[k] += x[n] * np.exp(-2.0 * np.pi * 1.0j / N ) ** (k * n) 
        
    return X


def sample(f, N=16, N_T=1):
    T = 2.0 * np.pi 
    omega = 2.0 * np.pi / T # i.e. omega=1 en estos ejemplos

    delta_t = T/N

    t = np.arange(N) * delta_t * N_T 
    x = f(t) 

    t_model = np.linspace(t.min(), t.max(), 1000)
    x_model = func(omega * t_model)
    return t, x, t_model, x_model




def func(t):
    return 3.0*np.cos(t) + 2.0*np.cos(3*t) + np.cos(5*t) 

t, x, t_model, x_model = sample(func)
X = FT(x)
N = len(X)

plt.figure(figsize=(8,4.0))
plt.subplot(1,2,1)

plt.scatter(t, x, label='sample')
plt.plot(t_model, x_model, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t)=3.0cos(t) + 2.0cos(3t) + cos(5t) ')
plt.grid()
plt.legend()


plt.subplot(1,2,2)
plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("N=16")
plt.grid()
plt.savefig('sample_1.png')


def func(t):
    return 3.0*np.cos(t) + 2.0*np.cos(3*t) + np.cos(5*t) 

t, x, t_model, x_model = sample(func, N=32)
X = FT(x)
N = len(X)

plt.figure(figsize=(8,4.0))
plt.subplot(1,2,1)

plt.scatter(t, x, label='sample')
plt.plot(t_model, x_model, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t)=3.0cos(t) + 2.0cos(3t) + cos(5t) ')
plt.grid()
plt.legend()


plt.subplot(1,2,2)
plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("N=32")
plt.grid()
plt.savefig('sample_2_a.png')


def func(t):
    return 3.0*np.cos(t) + 2.0*np.cos(3*t) + np.cos(5*t) 

t, x, t_model, x_model = sample(func, N=32, N_T=2)
X = FT(x)
N = len(X)

plt.figure(figsize=(8,4.0))
plt.subplot(1,2,1)

plt.scatter(t, x, label='sample')
plt.plot(t_model, x_model, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t)=3.0cos(t) + 2.0cos(3t) + cos(5t) ')
plt.grid()
plt.legend()


plt.subplot(1,2,2)
plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("N=32")
plt.grid()
plt.savefig('sample_2_b.png')


def func(t):
    return np.sin(t) + 2.0*np.sin(3*t) + 3*np.sin(5*t) 

t, x, t_model, x_model = sample(func)
X = FT(x)
N = len(X)

plt.figure(figsize=(8,4.0))
plt.subplot(1,2,1)

plt.scatter(t, x, label='sample')
plt.plot(t_model, x_model, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t)=sin(t) + 2.0sin(3t) + 3sin(5t) ')
plt.grid()
plt.legend()


plt.subplot(1,2,2)
plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("N=16")
plt.grid()
plt.savefig('sample_3.png')


def func(t):
    return 5*np.sin(t) + 2.0*np.cos(3*t) + np.sin(5*t) 

t, x, t_model, x_model = sample(func)
X = FT(x)
N = len(X)

plt.figure(figsize=(8,4.0))
plt.subplot(1,2,1)

plt.scatter(t, x, label='sample')
plt.plot(t_model, x_model, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t)=5sin(t) + 2cos(3t) + sin(5t) ')
plt.grid()
plt.legend()


plt.subplot(1,2,2)
plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("N=16")
plt.grid()
plt.savefig('sample_4.png')



def func(t):
    return 5 + 10*np.sin(t+2)

t, x, t_model, x_model = sample(func)
X = FT(x)
N = len(X)

plt.figure(figsize=(10,20))
plt.subplot(4,2,1)

plt.scatter(t, x, label='sample')
plt.plot(t_model, x_model, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t)=5 + 10sin(t+2)')
plt.grid()
plt.legend()


plt.subplot(4,2,2)
plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("N=16")
plt.grid()



def func(t):
    return 10*np.sin(t+2)

t, x, t_model, x_model = sample(func)
X = FT(x)
N = len(X)

plt.subplot(4,2,3)

plt.scatter(t, x, label='sample')
plt.plot(t_model, x_model, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t)=10sin(t+2)')
plt.grid()
plt.legend()


plt.subplot(4,2,4)
plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("N=16")
plt.grid()


def func(t):
    return np.sin(t+2)

t, x, t_model, x_model = sample(func)
X = FT(x)
N = len(X)

plt.subplot(4,2,5)

plt.scatter(t, x, label='sample')
plt.plot(t_model, x_model, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t)=sin(t+2)')
plt.grid()
plt.legend()


plt.subplot(4,2,6)
plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("N=16")
plt.grid()



def func(t):
    return np.sin(t)

t, x, t_model, x_model = sample(func)
X = FT(x)
N = len(X)

plt.subplot(4,2,7)

plt.scatter(t, x, label='sample')
plt.plot(t_model, x_model, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t)=sin(t)')
plt.grid()
plt.legend()


plt.subplot(4,2,8)
plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("N=16")
plt.grid()



plt.savefig('sample_5.png')



def func(t):
    return np.sin(0.25*t) + 5*np.sin(t)

t, x, t_model, x_model = sample(func, N_T=4, N=16)
X = FT(x)
N = len(X)

plt.figure(figsize=(8,9.0))
plt.subplot(2,2,1)

plt.scatter(t, x, label='sample')
plt.plot(t_model, x_model, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t)=sin(t/4) + 5 sin(t)')
plt.grid()
plt.legend()


plt.subplot(2,2,2)
plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("N=16")
plt.grid()


t, x, t_model, x_model = sample(func, N_T=4, N=8)
X = FT(x)
N = len(X)


plt.subplot(2,2,3)

plt.scatter(t, x, label='sample')
plt.plot(t_model, x_model, label='x(t)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('x(t)=sin(t/4) + 5 sin(t)')
plt.grid()
plt.legend()


plt.subplot(2,2,4)
plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("N=8")
plt.grid()



plt.savefig('sample_6.png')
