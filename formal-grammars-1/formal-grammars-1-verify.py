#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Jun  1 12:58:51 2020

Generative rules:
S --> NS + VS
NS --> A + N
VS --> V + NS


Check if a given sentences follows these rules. 

"""

# Get sentences from the database
def get_sentences(filename):
    F = open(filename).readlines()
    S_gen = [] # list of sentences
    for i in F:
        S_gen.append(i.split())
    
    return(S_gen)


# Convert data to a usable form
def create_dictionary(keys, list_of_words):
    d={}
    for i in range(len(keys)):
        d[keys[i]] = list_of_words[i]
    return(d)


# Find unique sentence structures
def get_structures(sentences, dictionary):
    
    # Putting structures together
    structures = []
    for i in sentences:
        s = []
        for j in i:
            for k in dictionary.keys():
                if j in dictionary[k]:
                    s.append(k)
        structures.append(s)

    # Finding unique structures
    M = []
    for s in structures:
        M.append(tuple(s))
    
    Mset = set(M)
    
    M = []
    for m in Mset:
        M.append(list(m))
    return(M)


# Find the number of matches
def results(S, test):
    # S = All the unique structures in the database
    c = 0
    for i in S:
        for j in test:
            if i == j:
                print('Test seq', j, 'is a match.')
                c = c + 1
    return(100*c/len(test))



# The procedure 
def main():
    
    # Open the file containinf sequences generated using rules.
    filename = 'formal-grammars-1-generated-sentences.txt'
    
    sentences = get_sentences(filename)
    
    # Dictionary
    Article = ['the', 'an', 'a']
    Noun = ['dog', 'computer', 'music', 'musician', 'coffee']
    Verb = ['composes', 'makes', 'hears']
    
    keys = ['Article', 'Noun', 'Verb']
    list_of_words = [Article, Noun, Verb]
    
    
    dictionary = create_dictionary(keys, list_of_words)
    S = get_structures(sentences, dictionary)
    
    
    # Test sequence
    test = [['the', 'dog', 'composes', 'a', 'dog'],['the', 'composes','dog','music','the']]
    test_structs = get_structures(test, dictionary)  
    
    print('Match Percentage: ', results(S, test_structs))
    


if __name__=='__main__':
    main()