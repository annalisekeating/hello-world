#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:46:10 2020

Markov-1, but, with sound.

Read probabilities from probabilities-markov-1-sound.txt
Use markov-1-text-file-sound.py to generate probabilities

"""

import numpy as n
import simpleaudio as sa


global a4, sample_rate, channels, duration
a4 = 440
sample_rate = 44100
channels = 2
duration = 1



# Play audio section
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
        


# Read the matrix from a text file.
# Generate the text file using markov-1-text-file.py
def get_matrix(filename):
    F = open(filename, 'r').readlines()
    C = F[0].split(',')
    choices = []
    for i in C:
        j = (i.split())[0]
        choices.append(j)

    probabilities = []
    for i in range(len(F)-1):
        p = F[i+1].split(',')
        q = []
        for i in p:
            q.append(float(i))
        probabilities.append(q)
    return(choices, probabilities)



# Find the next note using data read from the next file    
def next_note(current_note, choices, probabilities):
    i = choices.index(current_note)
    p = probabilities[i]
    next_note = n.random.choice(choices, p = p) 
    return(next_note)



# Switching to MIDI numbers from note names
def name2midi(note_name):
    note_names = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4']
    midi_nos = [48, 50, 52, 53, 55, 57, 59, 60]
    i = note_names.index(note_name)
    return(midi_nos[i])



# Putting everything together
def main():
    filename = 'probabilities-markov-1-sound.txt'
    C, probabilities = get_matrix(filename)
    
    choices = []
    for i in C:
        choices.append(name2midi(i))
    
    # first note
    stream = [52]
    no_of_notes = 32
    for i in range(no_of_notes - 1):
        next_no = next_note(stream[i], choices, probabilities)
        stream.append(next_no)
        
    print('Note Strea: ', stream)
    
    print('\nPlaying Stream')
    play_midi(stream)
    
    print('\nDone !')


if __name__ == '__main__':
    main()