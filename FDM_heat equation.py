import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#defining parameters, initial data
l = 1
span = 0.5
dx = 0.05
dt = 0.05
alpha = 0.05
g = alpha * dt / dx**2
print(g)

nx = int(l / dx) +1
nt = int(span / dt) +1

x = np.linspace(0,l,nx)
t = np.linspace(0,span,nt)
xm, tm = np.meshgrid(x, t)

#defining temperature matrix
T = np.zeros((nt,nx))

#defining boundary conditions 
#initial condition
a = np.arange(nx)
T[0] = np.sin(np.pi*a*dx/l)
#BC1 --> end conditions
T[:,0] = 0
T[:,-1] = 0

#filling the matrix T
for j in range(0,nt-1):
    for i in range(1,nx-1):

        T[j+1,i] = g * T[j,i+1] + (1 - 2 * g) * T[j,i] + g * T[j,i-1]
        
print(T)




#plotting
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_surface(xm, tm, T, rstride=1, cstride=1,
                cmap='winter', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('T')

plt.show()




















