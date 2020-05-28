#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:26:04 2020
"""

# play a midi note

# f = 2**((m−69)/12)*(440 Hz).
# m = 12*log2(f/440 Hz) + 69 


# to go one octave higher, add 12 to midi #


# the number of semitones from A4: 
# n  =  12*log2(fn/440 Hz)


import math
import numpy as n
import simpleaudio as sa
    
    
global a4, sample_rate
a4 = 432
sample_rate = 44100


def midi2freq(midinote):
    freq = 2**((midinote - 69)/12) * a4
    return(freq)


def freq2midi(freq):
    midinote = 12 * math.log2(freq/a4) + 69
    return(midinote)

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
    
    

inp = [53,54,55,56,57]

out = []
for i in inp:
    out.append(midi2freq(i))
    

out2 = []    
for j in out:
    out2.append(freq2midi(j))
    
    
print('\n', inp,'\n', out, '\n', out2, '\n')


print('playing the melody')
for i in inp:
    arr = midi2array(i, 1)
    play_audio(arr,2,sample_rate)
    
    
print('going one octave (12 semitones) higher')
for j in inp:
    arr = midi2array(j+12, 1)
    play_audio(arr, 2, sample_rate)
    
    
semitone = 6    
print('going '+str(semitone)+' higher')
for k in inp:
    arr = midi2array((k+semitone), 1)
    play_audio(arr, 2, sample_rate)
    
    
semitone = -4    
print('going '+str(semitone)+' lower')
for k in inp:
    arr = midi2array((k+semitone), 1)
    play_audio(arr, 2, sample_rate)
