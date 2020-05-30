#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 01:53:43 2020
"""

# uniform, linear, exponential, concave and convex distributions.

import random
import math


global upperlimit
upperlimit = 10 ** 4

def uniform(N):
    out = []
    for i in range(N):
        out.append(random.randint(1, upperlimit)/upperlimit)
    if N == 1:
        return(out[0])
    else:
        return(out)
    

def dist_fun(name, N):
    function_names = ['uniform', 'linear', 'exponential', 'concave', 'convex']
    if name not in function_names:
        print('Please check function name')
        return(None)
    if N <= 0:
        print('N has to be a positive integer')
        return(None)
    else:
        out = []
        for i in range(N):
            if name == 'uniform':
                out.append(uniform(1))
            if name == 'linear':
                x, y = uniform(2)
                if x > y:
                    out.append(x)
                else:
                    out.append(y)
            if name == 'exponential':
                lam = 0.5
                x = uniform(1)
                out.append(lam * math.e ** (-lam * x))
            if name == 'concave':
                lam = 1
                x = uniform(1)
                if x == 1:
                    x = uniform(1)
                else:
                    s = x * math.pi / 2
                    out.append(lam * math.tanh(s))
            if name == 'convex':
                x = 1; y = 2;
                r1 = 0; r2 = 0;
                s = 2
                while s > 1:
                    r1, r2 = uniform(2)
                    a = r1 ** (1/x)
                    b = r2 ** (1/y)
                    s = a + b
                out.append(a/s)
    if N == 1:
        return(out[0])
    else:
        return(out)




name = 'as'
x = dist_fun(name, 5)
print(x)