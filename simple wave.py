########################################################################################
#
#script that computes space-time evolution of a vibration spring modelled using 1-D wave equation 
#
#######################################################################################



import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


t_data = 0
dt = 0.5
x_data = np.linspace(0, 5, 50)
A = 1
l = 5
v = 1

s_comp = A * np.sin(np.pi * x_data / l)



def animate(i):

    plt.cla
    global t_data
    global s_comp

    y_data = s_comp * np.cos(np.pi * t_data * v / l)
    ax1.lines[0].set_data(x_data, y_data)
    ax1.texts[0].set_text("t={}".format(round(t_data,1)))
    
    
    
    t_data = round(t_data,1) + dt


    
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot([], [], linewidth=1, label="function")
ax1.set_xlim(0-0.1, l+0.1)
ax1.set_ylim(-1.1, +1.1)
##plt.legend(loc='upper left')
ax1.text(4.5, -1, "order={}".format(t_data), fontsize=9)
ax1.text(0.1, 0.9, r"$\frac{\partial^2 y}{\partial t^2} = \nu^2 \frac{\partial^2 y}{\partial x^2}$", fontsize=15)
##
ani = FuncAnimation(fig, animate, interval=100)
plt.show()
