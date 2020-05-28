#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:31:11 2020

Serial-1:
Take a MIDI sequence
Perform these operations: transpose, retrograde, inversion, retro_inversion
Play serquence

"""


import numpy as n
import simpleaudio as sa



global a4, sample_rate, channels, duration
a4 = 440
sample_rate = 44100
channels = 2
duration = 1


def midi2freq(midinote):
    freq = 2**((midinote - 69)/12) * a4
    return(freq)


def play_midi(midinotes):
    t = n.linspace(0, duration, duration * sample_rate, False)
    for i in midinotes:
        freq = midi2freq(i)
        audio = n.sin(freq * t * 2 * n.pi)
        audio *= 32767 / n.max(n.abs(audio))
        audio = audio.astype(n.int16)
        play_obj = sa.play_buffer(audio, 2, channels, sample_rate)
        play_obj.wait_done()

# transpose
def transpose(notes, no_of_semitones):
    out = []
    for i in notes:
        out.append(i+no_of_semitones)
    return(out)


# retrograde
def retrograde(notes):
    retro = []
    for i in range(len(notes)):
        retro.append(notes[len(notes)-i-1])
    return(retro)


#inversion
def inversion(notes): # ref 55
    diff = []
    for i in range((len(notes)-1)):
        diff.append(notes[i+1] - notes[i])
    notes_i = [notes[0]] # first note is the same
    for j in range(len(diff)):
        notes_i.append(notes_i[j] - diff[j])
    return(notes_i)


# retrograde-inversion
def retro_inversion(notes):
    notes_out = retrograde(notes)
    notes_out = inversion(notes_out)
    return(notes_out)


def main():
    notes = [62, 70, 68, 66, 65, 60, 58, 72, 70, 62, 70, 72]
    print('original: ', notes)
    print('Playing original sequence..')
    play_midi(notes)
    
    function_list = [transpose, retrograde, inversion, retro_inversion]
    
    no_of_semitones = 5
    
    for f in function_list:
        if f == transpose:
            out = f(notes, no_of_semitones)
            
        else:
            out = f(notes)
            
        print('\n'+f.__name__+' :', out)
        print('Playing Sequence...')
        play_midi(out)
    print('\nDone !')

if __name__ == '__main__':
    main()
