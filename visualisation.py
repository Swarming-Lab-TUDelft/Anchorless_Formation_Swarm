#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from itertools import count
from matplotlib.animation import FuncAnimation

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from waypoint_functions import *

def visualiseFormation(frame, n_drones):
    gen = generate_ver_rotating_lines

    # Initialize the figure and 3D axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Set to size of drone cage (ABS bounds)
    ax.set_xlim((-1.5, 1.75))
    ax.set_ylim((-1.84, 1.7))
    ax.set_zlim((0.0, 2.5))

    # Create labeled axes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


    # Create an empty scatter plot
    sc = ax.scatter([], [], [], c='b', marker='o')

    # Initialize the data and iterator
    data = np.empty((0, 3))
    colors = ['r', 'b', 'b', 'b', 'b', 'b'][:n_drones]
    labels = ['Leader', 'Follower', 'Follower','Follower','Follower','Follower'][:n_drones]
    # Function to update the scatter plot data
    def update(frame):
        nonlocal data
        nonlocal sc

        points = gen()[:n_drones, :]
        
        sc.remove()
        sc = ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=colors, marker='o', label='Leader')
        ax.legend()

    # Create an animation
    ani = FuncAnimation(fig, update, blit=False, interval=10)

    # Show the plot
    # plt.show()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().place(x = 20, y = 60, width= 410, height = 410)


