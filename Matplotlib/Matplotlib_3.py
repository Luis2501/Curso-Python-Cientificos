#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 16:26:35 2021

@author: luis
"""

#animation 

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np 

#f (x) = x**2

def f(x):
    
    return x**2

x = np.linspace(0, 4, 101)

fig = plt.figure()
ax = fig.gca()

def update(i):
    
    ax.clear()
    ax.plot(x[:i], f(x[:i]))
    ax.set_title(f"i = {i}")
    ax.set_ylim(min(f(x)), max(f(x)))
    ax.set_xlim(min(x), max(x))
    ax.grid()
    
ani = animation.FuncAnimation(fig, update, range(len(x)), interval=200)
ani.save("Animacion.mp4", fps=20)
plt.show()