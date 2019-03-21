import numpy as np
import matplotlib.pyplot as plt

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

def IFT(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        X[k] = 0.0j
        for n in range(N):
            X[k] += x[n] * np.exp(2.0 * np.pi * 1.0j / N ) ** (k * n) 
        
    return X/N

data = np.loadtxt("monthrg.dat")
time = data[:,0] + data[:,1]/12.0
signal = data[:,3]

signal = signal[time>1900]
time = time[time>1900]

# calculo la transformada
fft_signal = FT(signal)

# calculo la frecuencias
N=len(fft_signal)
f = np.zeros(N)
if N%2==0:
    f[:N//2] = np.arange(N//2)
    f[N//2:] = np.arange(-N//2,0)
else:
    f[:(N-1)//2+1] = np.arange((N-1)//2 + 1)
    f[(N-1)//2+1:] = np.arange(-(N-1)//2, 0)
d = (1.0/12.0) # intervalo entre medidas
f = f/(d*N)

# filtro de las frecuencias mayores que 0.2 years^{-1}
fft_signal_filter = fft_signal.copy()
fft_signal_filter[np.abs(f)>0.2] = 0.0


# calculo de la tranformada inversa
signal_filter = IFT(fft_signal_filter)

plt.figure(figsize=(8,14))

# plot de los datos
plt.subplot(4,1,1)
plt.scatter(time, signal, label='original', s=1.0)
plt.xlabel('Tiempo (yr)')
plt.ylabel('Numero manchas')
plt.grid()
plt.legend()

#plot de la transformada
plt.subplot(4,1,2)
plt.scatter(f, np.abs(fft_signal)/len(fft_signal), label='original', s=1.0)
plt.xlabel('Frecuencia (1/yr)')
plt.ylabel('Norma FFT / N')
plt.yscale('log')
plt.ylim([5E-3,1E2])
plt.grid()
plt.legend()

# plot de la transformada filtrada
plt.subplot(4,1,3)
plt.scatter(f, np.abs(fft_signal_filter)/len(fft_signal_filter), label='filtrado', s=1.0)
plt.xlabel('Frecuencia (1/yr)')
plt.ylabel('Norma FFT / N')
plt.yscale('log')
plt.grid()
plt.legend()
plt.ylim([5E-3,1E2])


# plot de la transformada inversa
plt.subplot(4,1,4)
plt.scatter(time, np.real(signal_filter), label='filtrado', s=1.0)
plt.xlabel('Tiempo (yr)')
plt.ylabel('Numero manchas')
plt.grid()
plt.legend()

plt.savefig('ejercicio18.png', bbox_inches='tight')
