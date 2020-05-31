#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:52:26 2020

Generate the text file
This file holds the first order markov chain for markov-1-no-sound.py
"""


F = open('probabilities-markov-1.txt','w')


F.write('A, B, C, D\n')
F.write('0.1, 0.2, 0.3, 0.4\n')
F.write('0.5, 0.1, 0.2, 0.2\n')
F.write('0.5, 0.2, 0.1, 0.2\n')
F.write('0.2, 0.2, 0.3, 0.3\n')


F.close() 
