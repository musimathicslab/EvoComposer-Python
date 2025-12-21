from music21 import *
import random
import os
import json
from utility.constants import KEY_SIGNATURES

VOICE_MAPPING = {
    "Soprano": 3,
    "Alto": 2,
    "Tenor": 1,
    "Bass": 0
}

class Chromosome:
    """In this context, a chromosome is a certain harmonization of the input melody that has either been built
    while initializing the population or obtained by crossover/mutation during the algorithm's epochs.
    """
    def __init__(self, melody, voice):
        self.melody = melody
        self.voice = voice

        bars = self.melody.getElementsByClass(stream.Measure)
        self.bars_count = len(bars)

        self.keySignature = self.melody.analyze("key")

        self.chords = []

        # Key signatures list (for modulation detection)
        self.chordKeySignatures = []

        self.voice_idx = VOICE_MAPPING[self.voice]
        
        # Init parts
        # Part objects to represent single voice parts
        self.soprano = stream.Part()
        self.alto = stream.Part()
        self.tenor = stream.Part()
        self.bass = stream.Part()
        
        self.soprano.id = "Soprano"
        self.alto.id = "Alto"
        self.tenor.id = "Tenor"
        self.bass.id = "Bass"

        self.score = stream.Score()
        self.score.append([self.soprano, self.alto, self.tenor, self.bass])

        # Harmonic and melodic quality
        self.harmonic_value = 0
        self.melodic_value = 0

        # Harmonize input melody
        self.harmonize()
    
    def harmonize(self):
        """Harmonizes input melody by assigning, for each note of the input melody, a note to every other part (besides the
        one specified in input) as to create a chord
        """
        
        measure_num = 1
        measure_offset = 0
        global_note_offset = 0

        # For each measure in the input melody line
        for meas in self.melody:
            bass_line = []
            tenor_line = []
            alto_line = []
            soprano_line = []
            
            # For each note in the measure
            for n in meas.notes:
                # Generate a chord
                bass, tenor, alto, soprano = self._build_random_chord(n)
                
                # Save the notes
                bass_note = n.transpose(bass)
                tenor_note = n.transpose(tenor)
                alto_note = n.transpose(alto)
                soprano_note = n.transpose(soprano)
                
                #print(measure_num, [bass_note.nameWithOctave, tenor_note.nameWithOctave, alto_note.nameWithOctave, soprano_note.nameWithOctave])

                # Add them to respective lines
                bass_line.append(bass_note)
                tenor_line.append(tenor_note)
                alto_line.append(alto_note)
                soprano_line.append(soprano_note)
            
                # Also add each chord to chord list
                # self.chords.append((bass_note, tenor_note, alto_note, soprano_note))
                self.chords.append(chord.Chord([bass_note, tenor_note, alto_note, soprano_note]))


            # For each part-line pair
            for part, line in zip([self.bass, self.tenor, self.alto, self.soprano], [bass_line, tenor_line, alto_line, soprano_line]):
                note_offset = 0
                # Create a new measure
                new_measure = stream.Measure(number=measure_num)
                
                # Add clef, key signature and time signature objects to first measure
                """
                if measure_num == 1:
                    # clef
                    if part.id == "Bass":
                        part_clef = clef.BassClef()
                    elif part.id == "Tenor":
                        part_clef = clef.TenorClef()
                    elif part.id == "Alto":
                        part_clef = clef.AltoClef()
                    elif part.id == "Soprano":
                        part_clef = clef.SopranoClef()
                    
                    new_measure.insert(offsetOrItemOrList=0, itemOrNone=part_clef)
                                        
                    # key signature
                    melody_tonic = str(self.keySignature).split()[0]
                    melody_mode = str(self.keySignature).split()[1]
                    new_measure.insert(offsetOrItemOrList=0, itemOrNone=key.Key(melody_tonic, melody_mode))
                    
                    # time signature
                    new_measure.insert(offsetOrItemOrList=0, itemOrNone=meter.TimeSignature("4/4"))
                """ 
                    
                
                # Fill it with the notes from the current line
                for n in line:
                    new_measure.insert(offsetOrItemOrList=global_note_offset + note_offset, itemOrNone=n)
                    note_offset += 1
                    
                # And add it to the current part
                part.insert(offsetOrItemOrList=measure_offset, itemOrNone=new_measure)
        
            measure_num += 1
            measure_offset += 4
            global_note_offset += 4


    def _build_random_chord(self, n):
        available_chords = []
        
        # Get diatonic notes in the scale of the key signature of the input melody
        s = self.keySignature.getScale()
        diatonic_notes = [str(p)[:-1] for p in scale.Scale.extractPitchList(s, comparisonAttribute="pitchClass")]
        
        # If note n is diatonic, choose a random chord that contains it among diatonic ones
        n_noOctave = n.nameWithOctave[:-1]

        # Load note chord atlas
        note_chord_atlas_path = os.path.join(".\\utility\\chord_atlases", n_noOctave + "_chord_atlas.json")
        with open(note_chord_atlas_path, "r") as file:
            note_chord_atlas = json.load(file)
        
        if n_noOctave in diatonic_notes:
            for cur_chord in note_chord_atlas[str(self.keySignature)]:
                if cur_chord[self.voice_idx] == 0 or cur_chord[self.voice_idx] == 12 or cur_chord[self.voice_idx] == -12:
                    available_chords.append((cur_chord, self.keySignature))
            
        # If note n is not diatonic, choose a random chord that contains it among all possible keys
        else:
            for key_signature in KEY_SIGNATURES:
                for cur_chord in note_chord_atlas[key_signature]:
                    if cur_chord[self.voice_idx] == 0 or cur_chord[self.voice_idx] == 12 or cur_chord[self.voice_idx] == -12:
                        key_tonic, key_mode = key_signature.split()
                        available_chords.append((cur_chord, key.Key(key_tonic, key_mode)))


        chosen_chord, chosen_chord_key = random.choice(available_chords)
        self.chordKeySignatures.append(chosen_chord_key)
        # print(f"chosen_chord: {chosen_chord}, chosen_chord_key: {chosen_chord_key}")
        return (*chosen_chord, )


    
    def _harmonic_evaluation(self):
        for i in range(len(self.chords)-1):
            c1 = self.chords[i]
            c2 = self.chords[i+1]
            print(f"c1: {c1}\nc2: {c2}")
            print(f"c1 normal order: {c1.normalOrder}")
            print(f"c2 normal order: {c2.normalOrder}")
            
            
            cur_key = self.chordKeySignatures[i]
            next_key = self.chordKeySignatures[i+1]
            print(f"cur_key: {cur_key}\nnext_key: {next_key}")
            
            
            # If two consecutive chords are in the same key signature
            if cur_key == next_key:
                # Roman numeral analysis
                rc1 = roman.romanNumeralFromChord(chord.Chord(c1.normalOrder), cur_key)
                rc2 = roman.romanNumeralFromChord(chord.Chord(c2.normalOrder), cur_key)

                print(f"rc1: {rc1.romanNumeralAlone}\nrc2: {rc2.romanNumeralAlone}")

                # If it's a major key
                if str(cur_key).split()[1] == "major":
                    print("c1 and c2 are in the same major key")
                    
                
                # Else, if it's a minor key
                else:
                    print("c1 and c2 are in the same minor key")
                        
            # Modulation
            else:
                print("c1 and c2 are in different keys")
            print()
        
    
    def _melodic_evaluation(self):
        pass

    def _evaluate(self):
        self._harmonic_evaluation()