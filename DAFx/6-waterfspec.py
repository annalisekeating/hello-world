#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:10:44 2020

Waterfspec in python

"""

# mandatory imports
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as n
import wavio
import custom_functions as c


# import a wavefile
filename = '_______.wav'
print('Reading Input..')
wavobj = wavio.read(filename)
x = wavobj.data
samplerate = wavobj.rate



# divide audio into fragments
frag_len = 0.020 # in seconds
frag_len = int(frag_len * samplerate)


print("Converting stereo to mono...")
sound = c.stereo2mono(x)


print("Normalizing the sound...")
sound = c.normalize(sound)


# Preprocessing, zero paddingt the last frag
print("Zero padding the signal..")
extra_samples = int(frag_len - (len(sound) % frag_len))
sound = n.hstack((sound, n.zeros((extra_samples,))))



print('Setting up the figure..')
fig = plt.figure(figsize=(16, 12), dpi =200)
ax = fig.gca(projection='3d')



# x axis denotes frequency
no_of_fft_pts = frag_len # or 16, 32, 256 etc.
end = int(no_of_fft_pts/2)

freq = (samplerate/1000)*n.fft.fftfreq(no_of_fft_pts)[0:end] # data is represented in kHz

# empty list for storing functions
verts = []
count = 0
no_of_frags = int(len(sound)/frag_len)
win = c.blackman_win(frag_len)


xs = freq
zs = n.linspace(0, no_of_frags-1, no_of_frags) # count


while count < no_of_frags:
    frag = sound[(count*frag_len):((count+1)*frag_len)] * win

    Y = n.abs(n.fft.fft(frag, no_of_fft_pts))
    Y = (Y/max(Y))[0:end]
    ys = n.hstack((0, Y, 0))

    verts.append(list(zip(xs, ys))) 
    
    # # Un-comment to plot individual fragments
    # fig = plt.figure()
    # plt.plot(freq, n.abs(Y))
    # plt.show()
    
    count = count + 1


print("Plotting..")
poly = PolyCollection(verts)
poly.set_alpha(0.7)
ax.add_collection3d(poly, zs=zs, zdir='y') # defining the axis



# setting axes limits
ax.set_xlabel('X = Frequency in kHz')
ax.set_xlim3d(0, max(freq))
ax.set_ylabel('Y = No of Fragments')
ax.set_ylim3d(0, no_of_frags)
ax.set_zlabel('Z = Amplitude')
ax.set_zlim3d(0, 1)

plt.show()




print("\nDone !")
