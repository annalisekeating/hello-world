#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:54:20 2020

Windows functions

- take a cosine signal
- Calulate spectrum
- Multiply cos signal with window
- Calc spectrum
- Plot everything
"""

import numpy as n
import matplotlib.pyplot as plt
import scipy.fftpack



def blackman_win(N):
    # N = no of points
    out = []
    for i in range(N):
        val = 0.42 - 0.5 * n.cos(2 * n.pi * i / N) + 0.08 * n.cos(4 * n.pi * i / N)
        out.append(val)
    return(out)


def hamming_win(N):
    # N = no of points
    out = []
    for i in range(N):
        val = 0.54 - 0.46 * n.cos(2 * n.pi * i /N)
        out.append(val)
    return(out)



# plotting the cosine signal
N = 1000
fsamp = 44100
t = n.linspace(0, N-1, N)
x = n.cos(2 * n.pi * 1000 * t/ fsamp)

plt.subplot(2,2,1)
plt.title('Cosine Signal')
plt.plot(t, x)



# plotting its spectrum
X = scipy.fftpack.fft(x, N)
X_mag = 20 * n.log10(n.abs(X))
f = n.linspace(0, 0.5, 500) # we only want the right half

plt.subplot(2,2,2)
plt.title('FFT of Cosine Signal')
plt.plot(f, X_mag[: int(N/2)]) # we only plot the right half


# signal with blackman window
N = 1000
b_win = blackman_win(N)
x = x * b_win

plt.subplot(2,2,3)
plt.title('Signal x window fn')
plt.plot(t, x)


#plotting the spectrum
X = scipy.fftpack.fft(x, N)
X_mag = 20 * n.log10(n.abs(X))
f = n.linspace(0, 0.5, 500) # we only want the right half

plt.subplot(2,2,4)
plt.title('FFT of after windowing')
plt.plot(f, X_mag[: int(N/2)]) # we only plot the right half

