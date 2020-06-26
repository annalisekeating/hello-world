#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:58:53 2020

file 1.3 pg 6

- Read input file (data and sampling freq)
- Perform sample-by-sample  alg y = a*x
- Write output into another file
"""

import wavio
import numpy as n


filename = '___.wav'

wavobj = wavio.read(filename)
print('Reading file: '+ filename)


x = wavobj.data
fs = wavobj.rate
row, col = x.shape


print('Performing Sample-by-sample operations')

y = n.zeros(x.shape)
for i in range(row):
    y[i] = 0.5 * x[i]
    

filename_new = filename.split('.')[0] + '-mod.wav'
print('Saving data to file: ' + filename_new)    
wavio.write(filename_new, y, fs, sampwidth = wavobj.sampwidth)
