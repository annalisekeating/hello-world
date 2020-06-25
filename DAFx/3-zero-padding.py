#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:19:20 2020

- Given: an 8 pt signal
- Get FFT
- Zero pad it ot make a 16 pt signal
- Get FFT
"""

import matplotlib.pyplot as plt
import numpy.fft
import numpy as n


# given 8 pt signal
N = 8
x = [-1, -0.5, 1, 2, 2, 1, 0.5, -1]
t = list(range(len(x)))

plt.subplot(2,2,1)
plt.title(str(len(x))+'-pt signal')
plt.stem(t,x)


# FFT of 8 pt signal
X_mag = n.abs(numpy.fft.fft(x))

plt.subplot(2,2,2)
plt.title(str(len(x))+'-pt FFT')
plt.stem(t, X_mag)



# Zero-padding x to get a 16 pt signal
N2 = 16
z = []
for i in range(N2 - N):
    z.append(0)
    
x = x + z
t = list(range(len(x)))

plt.subplot(2, 2, 3)
plt.title(str(len(x))+'-pt signal')
plt.stem(t, x)



# FFT of 16 pt signal
X_mag = n.abs(numpy.fft.fft(x))

plt.subplot(2,2,4)
plt.title(str(len(x))+'-pt FFT')
plt.stem(t, X_mag)