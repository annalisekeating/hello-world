#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:46:22 2020

Transformation

IF:
S(o) --> NS(n) + VS(m)
NS(n) --> A(n) + N(n)
VS(m) --> V + NS(m)

THEN:
S(t) --> NS(m) + VS(n)
NS(m) --> A(m) + N(m)
VS(n) --> NS(n) + V ... add punctuation NS(n) + ',' + V


Step 1: Verification (which is done in formal-grammars-1-verify)
Step 2: Find the sequence of words of one sentence
Step 3: Generate Next sentence accordingly

"""

# Get sentences from the database
def get_sentences(filename):
    F = open(filename).readlines()
    S_gen = [] # list of sentences
    for i in F:
        S_gen.append(i.split())
    
    return(S_gen)


# Making sentences look pretty
def good_looking(list_of_words):
    c = ''
    for i in list_of_words:
        if  list_of_words.index(i) == (len(list_of_words)-1):
            c = c + str(i) + '.'
        else:
            c = c + str(i) + ' '
        c = c.capitalize().replace(' ,', ',')
    return(c)



# Convert data to a usable form
def create_dictionary(keys, list_of_words):
    d={}
    for i in range(len(keys)):
        d[keys[i]] = list_of_words[i]
    return(d)



def transform_sentence(sentence, dictionary, print_struct):
    struct_name = []
    struct_no = []
    for j in sentence:
        for k in dictionary.keys():
            if j in dictionary[k]:
                struct_name.append(k)
                struct_no.append(dictionary[k].index(j))
    
    if print_struct == True:
        print(struct_name, struct_no)
                
    # the original sentence has 3 parts: NS + V + NS = one + two + three
    # the transformed sentence has 3 parts: NS + NS + V = three + one + two
     
    for i in range(len(struct_name)):
        if struct_name[i] == 'Verb':
            one = [sentence[i-2], sentence[i-1]]
            two = [sentence[i]]
            three = [sentence[i+1], sentence[i+2]]
    transformed_sent = three + [','] + one + two
    return(transformed_sent)



# Putting everything together
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
    # print(transform_sentence(trial, dictionary, True))
    
    
    for i in sentences[70:73]: # range selected at random
        print('Original: ', good_looking(i))
        
        transformed_sent = transform_sentence(i, dictionary, False)
        print('Transformed: ', good_looking(transformed_sent))
        
    
    # Saving transformed sentences
    F = open('formal-grammars-1-transformed-sentences.txt', 'w')
    
    
    for s in sentences:
        s = transform_sentence(s, dictionary, False)
        for i in s:
            F.write(i+' ') 
        F.write('\n')
    
if __name__ == '__main__':
    main()