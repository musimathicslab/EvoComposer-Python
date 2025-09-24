from music21 import *
import random
import copy
import os
import json
from utility.constants import MAJOR_KEY_CHORD_INFO, MINOR_KEY_CHORD_INFO

class Chromosome:
    """In this context, a chromosome is a certain harmonization of the input melody that has either been built
    while initializing the population or obtained by crossover/mutation during the algorithm's epochs.
    """
    def __init__(self, line, line_voice):
        # Create melody stream from input string
        self.line = line
        
        # Number of measures
        self.n_measures = len(self.line.getElementsByClass(stream.Measure))
        
        # Key signature
        self.keySignature = self.line.analyze("key")

        # Input melody line voice
        self.line_voice = line_voice
        
        # Voice mapping for chord selection
        self.voice_mapping = {
            "Soprano": 3,
            "Alto": 2,
            "Tenor": 1,
            "Bass": 0
        }
        self.voice_idx = self.voice_mapping[self.line_voice]
        
        # Init parts
        self._init_parts(self.line)
        
        self._init_score()
        
        # Harmonize input melody
        self.harmonize()
        
    
    def _init_parts(self, line):
        
        # Part objects to represent single voice parts
        self.soprano = stream.Part()
        self.alto = stream.Part()
        self.tenor = stream.Part()
        self.bass = stream.Part()
        
        self.soprano.id = "Soprano"
        self.alto.id = "Alto"
        self.tenor.id = "Tenor"
        self.bass.id = "Bass"
        
    
    def _init_score(self):
        """
        Create score rapresentation of melody and parts. The object contains four different Part objects for the Soprano, Alto, Tenor and Bass voices.
        This method is called only after harmonization of the input melody.
        
        Returns:
            stream.Score(): score object containing parts, measures and input melody.
        """
        self.score = stream.Score()

        # Add parts to Score object
        self.score.append([self.soprano, self.alto, self.tenor, self.bass])

    
    def harmonize(self):
        """Harmonizes input melody by assigning, for each note of the input melody, a note to every other part (besides the
        one specified in input) as to create a chord
        """
        
        measure_num = 1
        measure_offset = 0
        global_note_offset = 0

        # For each measure in the input melody line
        for meas in self.line:
            bass_line = []
            tenor_line = []
            alto_line = []
            soprano_line = []
            
            # For each note in the measure
            for n in meas.notes:
                # Generate a chord
                bass, tenor, alto, soprano = self._build_chord(n)
                
                # Save the notes
                bass_note = n.transpose(bass)
                tenor_note = n.transpose(tenor)
                alto_note = n.transpose(alto)
                soprano_note = n.transpose(soprano)
                
                #print(measure_num, [bass_note.nameWithOctave, tenor_note.nameWithOctave, alto_note.nameWithOctave, soprano_note.nameWithOctave])

                bass_line.append(bass_note)
                tenor_line.append(tenor_note)
                alto_line.append(alto_note)
                soprano_line.append(soprano_note)
            

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
        

    def _handle_7th_inversions(self, curr_chord, inv):
        before_inv = copy.deepcopy(curr_chord)
        
        # Invert voicing
        after_inv = before_inv[inv:] + before_inv[:inv]
        return after_inv
    
    
    def _handle_triad_inversions(self, curr_chord, inv):
        before_inv = copy.deepcopy(curr_chord)
        before_inv2 = copy.deepcopy(curr_chord)
        root = None
        fifth = None
        
        # If chord is in root position, double the root
        if inv == 0:
            root = curr_chord[0]
            before_inv.append(root)
    
        # If chord is in first inversion, create two instances of the chord
        # where one doubles the root and the other doubles the fifth
        elif inv == 1:
            root = curr_chord[0]
            fifth = curr_chord[2]
            
            before_inv.append(root)
            before_inv2.append(fifth)
        
        # If the chord is in second inversion, double the fifth
        elif inv == 2:
            fifth = before_inv[2]
            before_inv.append(fifth)

        # Invert voicing
        after_inv = before_inv[inv:] + before_inv[:inv]
        after_inv2 = None

        if inv == 1:
            after_inv2 = before_inv2[inv:] + before_inv2[:inv]
            return after_inv, after_inv2

        return after_inv, None


    def _get_inversions(self, n, curr_chord):
        popped_note = None

        # If note n_semitonesFromTonic is not the 7th in the current chord:
        # - keep an unaltered version
        # - create a new version by removing the 7th from the chord and doubling the root or the fifth
        
        if curr_chord[3] != n:
            chord_no7th = copy.deepcopy(curr_chord)
            # Remove last element (the 7th) from semitones list
            popped_note = chord_no7th.pop()
            
        # Else, note n_semitonesFromTonic is the 7th in the chord (no notes are removed)
        else:
            chord_no7th = None
            popped_note = None


        chord_inversions = []
        for inversion in [0, 1, 2, 3]:
            chord_inversions.append(self._handle_7th_inversions(curr_chord, inversion))
    
        if chord_no7th:
            for inversion in [0, 1, 2]:
                inv1, inv2 = self._handle_triad_inversions(chord_no7th, inversion)
                
                if inv2:
                    chord_inversions.append(inv1)
                    chord_inversions.append(inv2)
                else:
                    chord_inversions.append(inv1)
        
        return chord_inversions


    def _build_chord(self, n):
        available_chords = []
        
        # Get diatonic notes in the scale of the key signature of the input melody
        s = self.keySignature.getScale()
        diatonic_notes = [str(p)[:-1] for p in scale.Scale.extractPitchList(s, comparisonAttribute="pitchClass")]
        
        # If note is diatonic, choose a random chord that contains it among diatonic ones
        n_noOctave = n.nameWithOctave[:-1]

        # Load note chord atlas
        note_chord_atlas_path = os.path.join(".\\utility\\chord_atlases", n_noOctave + "_chord_atlas.json")
        with open(note_chord_atlas_path, "r") as file:
            note_chord_atlas = json.load(file)
        
        if n_noOctave in diatonic_notes:
            for cur_chord in note_chord_atlas[str(self.keySignature).capitalize()]:
                if cur_chord[self.voice_idx] == 0 or cur_chord[self.voice_idx] == 12 or cur_chord[self.voice_idx] == -12:
                    available_chords.append(cur_chord)
            
        # If note n is not diatonic, choose a random chord that contains it among all possible keys
        else:
            key_signatures = [
                "C major", "C# major", "D- major", "D major", "D# major", "E major", "F major", "F# major", "G- major", "G major", "G# major", "A- major", "A major", "A# major", "B- major", "B major",
                "C minor", "C# minor", "D- minor", "D minor", "D# minor", "E minor", "F minor", "F# minor", "G- minor", "G minor", "G# minor", "A- minor", "A minor", "A# minor", "B- minor", "B minor",
            ]

            for key_signature in key_signatures:
                for cur_chord in note_chord_atlas[key_signature]:
                    if cur_chord[self.voice_idx] == 0 or cur_chord[self.voice_idx] == 12 or cur_chord[self.voice_idx] == -12:
                        available_chords.append(cur_chord)

        chosen_chord = random.choice(available_chords)
        return (*chosen_chord, )
        

class EvoComposer:
    def __init__(self, line_string, line_voice, p_size=5, p_c=0.7, p_m=0.01, max_gen=100):
        # Create line stream from input TinyNotation string
        self.line = converter.parse(line_string)
        self.line_voice = line_voice
        
        # Population size
        self.p_size = p_size
        
        # Probability of crossover
        self.p_c = p_c
        
        # Probability of mutation
        self.p_m = p_m
        
        # Maximum number of generations
        self.max_gen = max_gen
        
        self.population = self.initialize_population()


    def initialize_population(self):
        """
        Initialize the population by creating p_size random harmonizations.
        """
        population = []
        
        for _ in range(self.p_size):
            c = Chromosome(self.line, self.line_voice)
            population.append(c)
        
        return population
        

    def evaluate(self):
        # Evaluate the fitness of each individual in the population
        pass


    def select_parents(self):
        # Select parents based on their fitness for reproduction
        pass


    def crossover(self, parent1, parent2):
        # Perform crossover between two parents to create offspring
        pass


    def mutate(self, individual):
        # Mutate an individual with a certain probability
        pass


    def run(self):
        # Run the evolutionary algorithm for a specified number of generations
        pass
