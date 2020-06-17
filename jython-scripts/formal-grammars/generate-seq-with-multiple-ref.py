'''
formal grammars - multiple reference notes

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
def create_pitch(ref, i, d):
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


# Going to select 5 refrences
ref_notes = [51, 52, 53, 54, 53, 52, 56]  


# For SEQ2
seq1 = Phrase(0.0)

# For SEQ2
seq2 = Phrase(0.0)


for r in range(len(ref_notes)):
   ref = ref_notes[r]

   pitches1 = [create_pitch(ref, 5,0), create_pitch(ref, 8,0), create_pitch(ref, 11,0)]
   durations1 = create_durations(pitches1)
   seq1.addNoteList(pitches1, durations1)
   
   
   pitches2 = [create_pitch(ref, 5,1), create_pitch(ref, 8,1)]
   durations2 = create_durations(pitches2)
   seq2.addNoteList(pitches2, durations2)


part1 = Part(STRINGS, 0) # empty strings part
part1.setTempo(60)

seq1.addNote((56+13), 1)
seq2.addNote((56+8), 1)

part1.addPhrase(seq1)
part1.addPhrase(seq2)
Play.midi(part1)
