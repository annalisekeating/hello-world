#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:09:23 2020

formal grammars. Coding as is, whatever is on p 75

Generative rules:
S --> NS + VS
NS --> A + N
VS --> V + NS

Generated sentences stored in db-formal-grammars-1.txt

"""


# Generative Rules
def sentence(noun_sent, verb_sent):
    sent = ns + vs
    return(sent)
    
    
def noun_sentence(article, noun):
    noun_sent = [article, noun]
    return(noun_sent)

def verb_sentence(verb, noun_sent):
    verb_sent = [verb]
    for ns in noun_sent:
        verb_sent.append(ns)
    return(verb_sent)



# Dictionary
A = ['the', 'an', 'a']
N = ['dog', 'computer', 'music', 'musician', 'coffee']
V = ['composes', 'makes', 'hears']



# Generating sentences
NS = [] # Noun Sentences
for a in A:
    for n in N:
        noun_sent = noun_sentence(a, n)
        NS.append(noun_sent)
        
        
VS = [] # Verb Sentences
for v in V:
    for ns in NS:
        verb_sent = verb_sentence(v, ns)
        VS.append(verb_sent)
        

S = [] # Sentences
for ns in NS:
    for vs in VS:
        sent = sentence(ns, vs)
        S.append(sent)



# Saving these sentences in a database/ text file
F = open('db-formal-grammars-1.txt', 'w')

for s in S:
    for i in s:
        F.write(i+',') 
    F.write('\n')
    

F.close()
