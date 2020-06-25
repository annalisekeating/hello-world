#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:25:02 2020

using spectogram
"""

import matplotlib.pyplot as plt
import wavio
import numpy as n
import custom_functions as c


filename = 'sunshine5.wav'
wavobj = wavio.read(filename)
x = wavobj.data
x = c.stereo2mono(x)


plt.subplot(2, 1, 1)
plt.title('audio signal')
plt.plot(x)




plt.subplot(2, 1, 2)
plt.title('Spectrogram')
plt.specgram(x, Fs = wavobj.rate)




