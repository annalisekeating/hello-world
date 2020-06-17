# Play notes simultaneously, # overlapping notes
# Playing two sequences simultaneously

from music import *

# first create a part. Part = what is going to holf phrases
part1 = Part(FLUTE, 0) # empty strings part
part1.setTempo(80)


# first sequence
ph = Phrase(0.0) 
pitches = [56, 58, 59]
durations = [0.66, 0.66, 0.66]
ph.addNoteList(pitches, durations)


# second sequence
ph2 = Phrase(1.0)
pitches2 = [53, 52]
durations2 = [1, 1]
ph2.addNoteList(pitches2, durations2)


# Putting the two together
part1.addPhrase(ph)
part1.addPhrase(ph2)



Play.midi(part1)
