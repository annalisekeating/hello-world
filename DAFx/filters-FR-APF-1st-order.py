#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 18:12:01 2020

"""

import numpy as n
from scipy import signal
import matplotlib.pyplot as plt



fs = 44100
fc = 0.1 * fs

c = (n.tan(n.pi * fc/ fs) - 1)/(n.tan(n.pi * fc/ fs) + 1)


# TF
b = [1, c]
a = [c, 1]

w, h = signal.freqz(b, a)


fig = plt.figure()
fig.suptitle('Frequency Response of a First Order All Pass Filter')
H = n.round(20 * n.log10(abs(h)))

w = w /(2* n.pi)

ax1 = fig.add_subplot(211)
ax1.plot(w, H, 'b')
ax1.set_ylabel('Magnitude (dB)')
ax1.set_xlabel('Frequency')
ax1.grid()


ax2 = fig.add_subplot(212)

angles = n.unwrap(-1*n.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle (radians)')
ax2.grid()

plt.show()