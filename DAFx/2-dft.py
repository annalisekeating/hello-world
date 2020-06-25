#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:22:29 2020

- Plot a cosine signal
- find its fft at N=16, N=1024
- Plot the results
"""

import numpy as n
import numpy.fft
import matplotlib.pyplot as plt


# signal
N = 16
t = n.linspace(0, N-1, N)
x = n.cos(2 * n.pi * 2 * t/N)

# plotting the signal
plt.subplot(3, 1, 1)
plt.stem(t, x)


# FFT for 16 points
X = n.fft.fft(x)
X_mag = n.abs(X)/N

plt.subplot(3, 1, 2)
plt.stem(t, X_mag)


# FFT for 1024 points
N = 1024
t = n.linspace(0, N-1, N)
x = n.cos(2 * n.pi * 2 * t/N)
X = n.fft.fft(x)
X_mag = n.abs(X)/N

plt.subplot(3, 1, 3)
plt.stem(t, X_mag)
plt.show()