# just playing a simple melody sequentially

from music import *

pitches = [53, 54, 57, REST, 52, REST]
durations = [1, 0.3, 0.25, 0.4, 0.2, 1]

pitches2 = [57, 53, 57, 54, REST, 52, REST]
durations2 = [0.2, 0.25, 0.2, 0.3, 0.4, 0.2, 0.5]

pitches3 = [57, 52, 57, 54, REST]
durations3 = [0.2, 0.25, 0.2, 0.3, 0.4]


phr = Phrase()

for i in range(3):
   phr.addNoteList(pitches, durations)
   phr.addNoteList(pitches2, durations2)

phr.addNoteList(pitches, durations)
phr.addNoteList(pitches3, durations3)


part1 = Part("a flute part on channel 0", FLUTE, 0)
part1.setTempo(90)
part1.addPhrase(phr)

Play.midi(part1)
