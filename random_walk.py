#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy as n
import simpleaudio as sa


global a4, sample_rate
a4 = 432
sample_rate = 44100



def midi2freq(midinote):
    freq = 2**((midinote - 69)/12) * a4
    return(freq)


def midi2array(midinote, duration): # duration in seconds
    t = n.linspace(0, duration, duration * sample_rate, False)
    freq = midi2freq(midinote)
    s = n.sin(freq * t * 2 * n.pi)
    return(s)


def play_audio(audio, channels, sample_rate):
    audio *= 32767 / n.max(n.abs(audio))
    audio = audio.astype(n.int16)
    play_obj = sa.play_buffer(audio, 2, channels, sample_rate)
    play_obj.wait_done()


a = [0,1,2,3,4,5,6,7,8,9,10,11]

seed = random.randint(0,len(a))

steps = [seed]

len_comp = 64 # number of notes

startnote = 53
for i in range(len_comp):
    boop = random.randint(0,1)
    if boop == 0:
        next1 = steps[i] + 1
        if next1 > len(a):
            next1 = next1 - 2
    else:
        next1 = steps[i] - 1
        if next1 < 0:
            next1 = next1 + 2
    steps.append(next1)
    
# print(steps)

midinotes=[]
for i in steps:
    midinotes.append(i+startnote)
    
print(midinotes)

print('Playing midi notes')

duration = 1 # second
for i in midinotes:
    arr = midi2array(i, duration)
    play_audio(arr,2,sample_rate)
    
print('Done !')
