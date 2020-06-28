#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:14:57 2020

Filters - FR - HPF - 1st order

HPF --> 1/2 * (1 - A(z))
"""

import numpy as n
from scipy import signal
import matplotlib.pyplot as plt



fs = 44100
fc = 0.1 * fs

c = (n.tan(n.pi * fc/ fs) - 1)/(n.tan(n.pi * fc/ fs) + 1)


# TF
b = [1-c, -1+c]
a = [2, 2*c]

w, h = signal.freqz(b, a)

w = w/ (2 * n.pi)

fig = plt.figure()
fig.suptitle('Frequency Response of a 1st order HPF')

H = 20 * n.log10(abs(h))



ax1 = fig.add_subplot(211)
ax1.plot(w, H, 'b')
ax1.set_ylabel('Magnitude (dB)')
ax1.set_ylim([-10, 1])
ax1.set_xlabel('Frequency')
ax1.grid()


ax2 = fig.add_subplot(212)

angles = n.unwrap(n.angle(h))
ax2.plot(w, n.angle(h), 'g')
ax2.set_ylabel('Angle (radians)')
ax2.grid()

plt.show()
