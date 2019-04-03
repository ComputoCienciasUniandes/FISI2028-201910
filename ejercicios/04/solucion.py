import numpy as np
import matplotlib.pyplot as plt

def petalo(r=1.0):
    # parte derecha de un petalo
    theta = np.linspace(+np.pi/6.0, -np.pi/6.0, 100)
    x = r * np.cos(theta) - r*np.cos(np.pi/6.0)
    y = r * np.sin(theta) 

    # parte izquierda del petalo
    x = np.append(x,-x)
    y = np.append(y,-y)
    return x, y

def rotacion(x, y, theta):
    new_x = x * np.cos(theta) - y * np.sin(theta)
    new_y = x * np.sin(theta) + y * np.cos(theta)
    return new_x, new_y

def desplazamiento(x, y, delta_x, delta_y):
    return x + delta_x, y + delta_y

def plot_circle(center_x, center_y, r=1.0):
    x_a, y_a = petalo(r=r)
    x, y = rotacion(x_a, y_a, -np.pi/3.0)
    x, y = desplazamiento(x, y, -x.max(), 0.25)

    x = np.append(x_a, x)
    y = np.append(y_a, y)

    x, y = desplazamiento(x, y, 0.0, 0.5)
    #plt.plot(x_a, y_a)

    for i in range(6):
        x_tmp, y_tmp = rotacion(x, y, i*np.pi/3.0)
        plt.plot(x_tmp+center_x, y_tmp+center_y, c='black')

def plot_flower(r=1.0):
    r=1.0
    delta_x = r * np.cos(np.pi/6.0)
    delta_y = 0.5*r

    plot_circle(0.0, 0.0, r=r)    
    for i in (-1,1):
        for j in (-1, 1):
            plot_circle(0.0 + i*delta_x, 0.0 + j*3.0*delta_y) 
            plot_circle(0.0 + i*2.0*delta_x, 0.0) 
            plot_circle(0.0 + i*2.0*delta_x, 0.0 + j*2.0*delta_y) 
            plot_circle(0.0, 0.0 + j*2.0*delta_y) 
            plot_circle(0.0, 0.0 + j*4.0*delta_y) 
            
plt.figure(figsize=(8,10))
ax = plt.axes()

plot_flower(r=10)
ax.set_aspect("equal")
_ = plt.axis('off')
plt.savefig("flordelavida.png")