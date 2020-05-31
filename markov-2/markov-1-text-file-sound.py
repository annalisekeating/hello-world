#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:48:20 2020

markov chain example for notes of C major scale

Probabilities
• if C3, then either C3, D3, E3, G3 or C4
• if D3, then either C3, E3 or G3
• if E3, then either D3 or F3
• if F3, then either C3, E3 or G3
• if G3, then either C3, F3, G3 or A3
• if A3, then B3
• if B3, then C4
• if C4, then either A3 or B3

markov-1-text-file-sound.py
"""

F = open('probabilities-markov-1-sound.txt','w')


F.write('C3, D3, E3, F3, G3, A3, B3, C4\n')
F.write('0.20, 0.20, 0.20, 0.00, 0.20, 0.00, 0.00, 0.20\n')
F.write('0.3333333333333333, 0.00, 0.3333333333333333, 0.00, 0.3333333333333333, 0.00, 0.00, 0.00\n')
F.write('0.00, 0.50, 0.00, 0.50, 0.00, 0.00, 0.00, 0.00\n')
F.write('0.3333333333333333, 0.00, 0.3333333333333333, 0.00, 0.3333333333333333, 0.00, 0.00, 0.00\n')
F.write('0.25, 0.00, 0.00, 0.25, 0.25, 0.25, 0.00, 0.00\n')
F.write('0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 0.00\n')
F.write('0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00\n')
F.write('0.00, 0.00, 0.00, 0.00, 0.00, 0.50, 0.50, 0.00\n')


F.close()
