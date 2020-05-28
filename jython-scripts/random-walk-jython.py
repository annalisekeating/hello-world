from music import *
import random

a = [0,1,2,3,4,5,6,7,8,9,10,11]

seed = random.randint(0,len(a))

steps = [seed]

len_comp = 64 # number of notes

startnote = 53
for i in range(len_comp):
    boop = random.randint(0,1)
    if boop == 0:
        next1 = steps[i] + 1
        if next1 > len(a):
            next1 = next1 - 2
    else:
        next1 = steps[i] - 1
        if next1 < 0:
            next1 = next1 + 2
    steps.append(next1)
    
# print(steps)

pitches=[]
for i in steps:
    pitches.append(i+startnote)

print('Playing midi notes')    
print(pitches)


phr = Phrase()

for p in pitches:
   n = Note(p, SN)    # create note with next pitch
   phr.addNote(n)    # and add it to phrase

Play.midi(phr)

print('Done !')
