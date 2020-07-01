#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:22:35 2020

1-D Automata

Rule: EX-OR
"""


import numpy as n
import matplotlib.pyplot as plt
# %matplotlib inline

from matplotlib.pyplot import figure
figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

block = n.array([0.0,0.0,0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0])
c = n.arange(1, len(block)-1, 1)


no_of_states = 45

rows = no_of_states
cols = len(block)

z = n.zeros((rows, cols))


first_state = block


N = 1 # magnitude
for j in range(rows):
    first = block[0]
    last = block[len(block)-1]
    next_state = n.zeros(n.shape(block))

    next_state[0] = first
    for i in c:
        left = block[i-1]
        right = block[i+1]
        if right == left:
            next_state[i] = 0
        else:
            next_state[i] = 1
        
    next_state[len(block)-1] = last

    block = next_state
    z[j, :] = next_state
    
z = n.vstack((first_state, z))
# print(z)

rows, cols = n.shape(z)
print(rows, cols)
for i in range(rows):
    block = z[i, :]
    for j in range(len(block)):
        if block[j] == 1:
            col = 'white'
        if block[j] == 0:
            col = 'black'
        rectangle = plt.Rectangle((N*j, -1*N*i), N, N, fc = col, ec='brown')
        plt.gca().add_patch(rectangle)

plt.axis('scaled')
plt.axis('off')
plt.show()
