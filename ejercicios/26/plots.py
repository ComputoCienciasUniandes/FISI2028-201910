import numpy as np
import matplotlib.pyplot as plt

data_euler = np.loadtxt("euler.dat")
data_rk = np.loadtxt("rk4.dat")
data_lf = np.loadtxt("leapfrog.dat")

plt.figure(figsize=(10,10))

# Position
max_t=2.0*2.0*np.pi
plt.subplot(3,3,1)
plt.plot(data_euler[:,0], data_euler[:,1])
plt.title("Euler")
plt.xlabel("Time")
plt.ylabel("Position")
plt.ylim([-1.5, 1.5])
plt.xlim([0, max_t])


plt.subplot(3,3,2)
plt.plot(data_rk[:,0], data_rk[:,1])
plt.title("RK")
plt.xlabel("Time")
plt.ylim([-1.5, 1.5])
plt.xlim([0, max_t])


plt.subplot(3,3,3)
plt.plot(data_lf[:,0], data_lf[:,1])
plt.title("Leap Frog")
plt.xlabel("Time")
plt.ylim([-1.5, 1.5])
plt.xlim([0, max_t])

# Velocity

plt.subplot(3,3,4)
plt.plot(data_euler[:,0], data_euler[:,2])
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.ylim([-1.5, 1.5])
plt.xlim([0, max_t])

plt.subplot(3,3,5)
plt.plot(data_rk[:,0], data_rk[:,2])
plt.xlabel("Time")
plt.ylim([-1.5, 1.5])
plt.xlim([0, max_t])

plt.subplot(3,3,6)
plt.plot(data_lf[:,0], data_lf[:,2])
plt.xlabel("Time")
plt.ylim([-1.5, 1.5])
plt.xlim([0, max_t])

# Phase space

plt.subplot(3,3,7)
plt.plot(data_euler[:,1], data_euler[:,2])
plt.xlabel("Position")
plt.ylabel("Velocity")
plt.xlim([-2.0, 2.0])
plt.ylim([-2.0, 2.0])

plt.subplot(3,3,8)
plt.plot(data_rk[:,1], data_rk[:,2])
plt.xlabel("Position")
plt.xlim([-2.0, 2.0])
plt.ylim([-2.0, 2.0])


plt.subplot(3,3,9)
plt.plot(data_lf[:,1], data_lf[:,2])
plt.xlabel("Position")
plt.xlim([-2.0, 2.0])
plt.ylim([-2.0, 2.0])




plt.savefig("plot.png")
