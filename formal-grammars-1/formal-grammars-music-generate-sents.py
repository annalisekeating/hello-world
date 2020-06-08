#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:11:59 2020

- Many reference notes
- Generating all possible sentences

Rules:
SEQ1 --> (I5, D1) + (I8, D1) + (I11, D1)
SEQ2 --> (I5, D2) + (I8, D2)
SIM1 --> SEQ1 + SEQ2

"""

# Create a note
def get_note(R, interval, direction):
    if direction == 'upwards':
        out = R + interval
    elif direction == 'downwards':
        out = R - interval
    else:
        out = R
        
    if out > 127 or out < 0:
        return([])
    else:
        return([out])



# Defining words

# Reference notes
R = []
for i in range(128):
    R.append(i)
    
# Intervals
I = []
for i in range(13):
    I.append(i)
    

# Durations
D = ['upwards', 'downwards', 'none']



# Creating Sentences
SIM = []
for r in R:
    # SEQ1 --> (I5, D1) + (I8, D1) + (I11, D1)
    seq1 = get_note(r, I[4], D[0]) + get_note(r, I[7], D[0]) + get_note(r, I[10], D[0])
    time1 = [0.3333333333333333, 0.3333333333333333, 0.3333333333333333]

    # SEQ2 --> (I5, D2) + (I8, D2)
    seq2 = get_note(r, I[4], D[1]) + get_note(r, I[7], D[1])
    time2 = [0.5, 0.5]
    
    if len(seq1) == 3 and len(seq2) == 2:
        SIM.append([r, seq1, time1, seq2, time2])
        
        
# saving sentences
F = open('formal-grammars-music-generated-sents.txt', 'w')

for s in SIM:
    s = str(s)+'\n'
    F.write(s)
    
F.close()