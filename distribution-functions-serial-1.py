#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:52:29 2020

# probablity distribution + sequences (ref. serial-1.py and distribution-functions.py


Create segments
- Generate 5 probablities, sum of all probablities  = 1
- Assign an operation to each segment (range)


Compositional Process:
- Generate random numbers
- Pick an operation based on where the number falls on the sequence
- Play sequences


"""

import numpy as n
import simpleaudio as sa
import random



global a4, sample_rate, channels, duration
a4 = 440
sample_rate = 44100
channels = 2
duration = 1


## PLAY MIDI

def midi2freq(midinote):
    freq = 2**((midinote - 69)/12) * a4
    return(freq)


def play_midi(midinotes):
    t = n.linspace(0, duration, int(duration * sample_rate), False)
    
    for i in midinotes:
        freq = midi2freq(i)
        audio = n.sin(freq * t * 2 * n.pi)
        audio *= 32767 / n.max(n.abs(audio))
        audio = audio.astype(n.int16)
        play_obj = sa.play_buffer(audio, 2, channels, sample_rate)
        play_obj.wait_done()
        
 
        
## OPERATIONS to be performed on sequences
 
def operation(name, notes, no_of_semitones):
    out = []
    
    if name == 'original':
        out = notes
    
    if name == 'transpose':
        for i in notes:
            out.append(i+no_of_semitones)
            
            
    if name == 'retrograde':
        for i in range(len(notes)):
            out.append(notes[len(notes)-i-1])
            
            
    if name == 'inversion':
        diff = []
        for i in range((len(notes)-1)):
            diff.append(notes[i+1] - notes[i])
        notes_i = [notes[0]] # first note is the same
        for j in range(len(diff)):
            notes_i.append(notes_i[j] - diff[j])
        out = notes_i
            
            
    if name == 'retrograde-inversion':
        one = []
        for i in range(len(notes)):
            one.append(notes[len(notes)-i-1])
        diff = []
        for i in range((len(notes)-1)):
            diff.append(notes[i+1] - notes[i])
        notes_i = [notes[0]] # first note is the same
        for j in range(len(diff)):
            notes_i.append(notes_i[j] - diff[j])
        out = notes_i
        
    if name == 'none':
        out = name
        
    return(out)



## PROBABLITY-related functions

# Generate 5 p such that their sum is 1
def uniform(N):
    out = []
    for i in range(N):
        out.append(random.randint(1, 10**4)/10**4)
    if N == 1:
        return(out[0])
    else:
        return(out)

# Creating a segment with N parts
def segment(N):
    seg = uniform(N-1)
    while sum(seg) > 1:
        seg = uniform(N-1)
    seg.append(1-sum(seg))
    return(seg)



## THE PROCESS that combines proablity 
def process(notes, functions, semitones, seg, points, play_notes):
    OUT = []
    for i in points:
        # print(i)
        if 0 <= i < seg[0]:
            out = operation('original', notes, 0)
            print('Original: ', out)
        elif seg[0] <= i < seg[1]:
            out = operation('transpose', notes, semitones[0])
            print('Transposition 3: ', out)
        elif seg[1] <= i < seg[2]:
            out = operation('transpose', notes, semitones[1])
            print('Transposition 5: ', out)
        elif seg[2] <= i < seg[3]:
            out = operation('retrograde', notes, 0)
            print('Retrograded: ', out)
        elif seg[3] <= i < seg[4]:
            out = operation('inversion', notes, 0)
            print('Inverted: ', out)
        else:
            out = operation('retrograde-inversion', notes, 0)
            print('Retro-inverted: ', out)   
            
        # the output of one operation becomes the input of the next
        notes = out
        OUT.append(out)
        
        if play_notes == True:
            play_midi(out)
    return(OUT)



def main():
    notes = [52, 60, 58, 56, 55, 50, 48, 62, 60, 52, 60, 62]
    
    
    function_list = ['original','transpose', 'retrograde', 'inversion', 'retrograde-inversion']
    semitones = [3, 5]
    
    seg = segment(5)
    
    points = uniform(5)


    process(notes, function_list, semitones, seg, points, play_notes = True)
    
    print('\nDone !')
    

if __name__ == '__main__':
    main()