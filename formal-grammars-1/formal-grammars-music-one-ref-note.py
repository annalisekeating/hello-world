#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:40:32 2020

One reference note

SEQ1 --> (I5, D1) + (I8, D1) + (I11, D1)
SEQ2 --> (I5, D2) + (I8, D2)
SIM1 --> SEQ1 + SEQ2


"""

global R
R = 54


# Create note
def get_note(interval, direction):
    if direction == 'upwards':
        out = R + interval
    elif direction == 'downwards':
        out = R - interval
    else:
        out = R
    return([out])



# Defining words
    
# Intervals
I = []
for i in range(13):
    I.append(i)
    

# Durations
D = ['upwards', 'downwards', 'none']



# Creating Sentences

# SEQ1 --> (I5, D1) + (I8, D1) + (I11, D1)
seq1 = get_note(I[4], D[0]) + get_note(I[7], D[0]) + get_note(I[10], D[0])

# SEQ2 --> (I5, D2) + (I8, D2)
seq2 = get_note(I[4], D[1]) + get_note(I[7], D[1])

sim1 = [seq1, seq2]
