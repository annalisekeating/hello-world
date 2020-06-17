'''
formal grammars - one reference note

Rules:
SIM1 → SEQ1 + SEQ2
SEQ1 → (I5, D1) + (I8, D1) + (I11, D1)
SEQ2 → (I5, D2) + (I8, D2)

generate sequences 1 and 2. Then put the two sequences in one part (sim)

'''

# some mandatory imports
from __future__ import division
from music import *


### Defining some functions before we proceed
def create_pitch(i, d):
   if D[d] == 'upwards':
      out = ref + I[i]
   elif D[d] == 'downwards':
      out = ref + I[i]
   elif D[d] == 'none':
      out = ref
   else:
      print('invalid entry')
   return(out)

def create_durations(pitches):
   durations = []
   for i in range(len(pitches)):
      durations.append(2/len(pitches))
   return(durations)

# The lexicon of this grammar: I, D

# Intervals 'I' ranging from 0 to 12
I = []
for i in range(13):
   I.append(i)
   
# Directions 'D'
D = ['upwards', 'downwards', 'none']


# Reference point
ref = 46


# For SEQ1
seq1 = Phrase(0.0)
pitches1 = [create_pitch(5,0), create_pitch(8,0), create_pitch(11,0)]
durations1 = create_durations(pitches1)
seq1.addNoteList(pitches1, durations1)


# For SEQ2
seq2 = Phrase(0.0)
pitches2 = [create_pitch(5,1), create_pitch(8,1)]
durations2 = create_durations(pitches2)
seq2.addNoteList(pitches2, durations2)

# Sim1
sim1 = Part(FLUTE, 0) # empty strings part
sim1.setTempo(80)
sim1.addPhrase(seq1)
sim1.addPhrase(seq2)

Play.midi(sim1)
