#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import count
from matplotlib.animation import FuncAnimation

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Boundaries
x1 = -1.50; x2 = 1.75;
y1 = -1.84; y2 = 1.70;
z1 =  0.00; z2 = 2.50;


initialised = False;

def previewFormation(frame, n_drones, dx, dy, dz):
    if initialised: # Destroy to redraw
        canvas.get_tk_widget().destroy()

    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
   
    sc = ax.scatter(0, 0, z2/2, c='r', marker='o', label='Leader')
    sc = ax.scatter(dx[:n_drones-1], dy[:n_drones-1], [z + z2/2 for z in dz[:n_drones-1]], c='b', marker='o', label='Follower')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim((x1, x2))
    ax.set_ylim((y1, y2))
    ax.set_zlim((z1, z2))
    ax.legend(loc=(0.75, 0.95))

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().place(x = 20, y = 60, width= 410, height = 410)










# def visualiseFormation_old(frame, n_drones):
#     gen = generate_ver_rotating_lines

#     # Initialize the figure and 3D axes
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     # Set to size of drone cage (ABS bounds)

#     # Create labeled axes
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')


#     # Create an empty scatter plot
#     sc = ax.scatter([], [], [], c='b', marker='o')

#     # Initialize the data and iterator
#     data = np.empty((0, 3))
#     colors = ['r', 'b', 'b', 'b', 'b', 'b'][:n_drones]
#     labels = ['Leader', 'Follower', 'Follower','Follower','Follower','Follower'][:n_drones]
#     # Function to update the scatter plot data
#     def update(frame):
#         nonlocal data
#         nonlocal sc

#         points = gen()[:n_drones, :]
        
#         sc.remove()
#         sc = ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=colors, marker='o', label='Leader')
#         ax.legend()

#     # Create an animation
#     ani = FuncAnimation(fig, update, blit=False, interval=10)

#     # Show the plot
#     # plt.show()
#     canvas = FigureCanvasTkAgg(fig, master=frame)
#     canvas.draw()
#     canvas.get_tk_widget().place(x = 20, y = 60, width= 410, height = 410)
#     initialised = True

