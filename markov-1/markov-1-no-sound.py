#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun May 31 15:59:24 2020

markov chains, simple.

- Given: Current note
- Play the next note according to pre-decided probabilities
- Create a loop around this task
- Create a stream

"""


import numpy as n


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


# put everything together and generete a stream of notes
def main():
    
    filename = 'probabilities-markov-1.txt'
    choices, probabilities = get_matrix(filename)
    
    # start note
    current_note = 'A'
    
    stream = [current_note]
    for i in range(8):
        next_no = next_note(stream[i], choices, probabilities) # next note depends on the previous note
        stream.append(next_no)
        
    print('Note Stream: ', stream)
    


if __name__ == '__main__':
    main()