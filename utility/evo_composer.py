from music21 import *
import random
import copy
from utility.constants import MAJOR_KEY_CHORD_INFO, MINOR_KEY_CHORD_INFO

class Chromosome:
    """In the context, a chromosome is a certain harmonization of the input melody that has either been built
    while initializing the population or obtained by crossover/mutation during the algorithm's epochs.
    """
    def __init__(self, input_melody_string, input_melody_voice):
        # Create melody stream from input string
        self.input_melody_string = input_melody_string
        self.melody_stream = converter.parse(self.input_melody_string)
        
        # Key signature
        self.keySignature = self.melody_stream.analyze("key")

        # Input melody voice
        self.input_melody_voice = input_melody_voice
        self.voice_mapping = {
            "Soprano": 3,
            "Alto": 2,
            "Tenor": 1,
            "Bass": 0
        }
        self.voice_idx = self.voice_mapping[self.input_melody_voice]
        
        # Init parts
        #self._init_parts(converter.parse(self.input_melody_string))
        self._init_parts(self.melody_stream)
        
        # Harmonize input melody
        self.harmonize()
        
    
    def _init_parts(self, melody_stream):
        
        # Part objects to represent single voice parts
        self.soprano = stream.Part()
        self.soprano.id = "Soprano"
        
        self.alto = stream.Part()
        self.alto.id = "Alto"
        
        self.tenor = stream.Part()
        self.tenor.id = "Tenor"
        
        self.bass = stream.Part()
        self.bass.id = "Bass"
        
        # Assign input melody to correct part
        if self.input_melody_voice == "Soprano":
            self.soprano = melody_stream
        
        elif self.input_melody_voice == "Alto":
            self.alto = melody_stream
        
        elif self.input_melody_voice == "Tenor":
            self.tenor = melody_stream
        
        elif self.input_melody_voice == "Bass":
            self.bass = melody_stream

    
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
        #print(self.keySignature)
        # For each measure in the input melody
        bass = tenor = alto = soprano = []

        for meas in self.melody_stream:
            # For each note in the measure
            for n in meas.notes:
                bass, tenor, alto, soprano = self._build_chord(n)
                print(f"bass: {n.transpose(bass)}")
                print(f"tenor: {n.transpose(tenor)}")
                print(f"alto: {n.transpose(alto)}")
                print(f"soprano: {n.transpose(soprano)}")


    def _handle_7th_inversions(self, chord, inv):
        before_inv = copy.deepcopy(chord)
        
        # Invert voicing
        after_inv = before_inv[inv:] + before_inv[:inv]
        return after_inv
    
    
    def _handle_triad_inversions(self, chord, inv):
        before_inv = copy.deepcopy(chord)
        before_inv2 = copy.deepcopy(chord)
        root = None
        fifth = None
        
        # If chord is in root position, double the root
        if inv == 0:
            root = chord[0]
            before_inv.append(root)
    
        # If chord is in first inversion, create two instances of the chord
        # where one doubles the root and the other doubles the fifth
        elif inv == 1:
            root = chord[0]
            fifth = chord[2]
            
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
        


    def _get_inversions(self, n, chord):
        popped_note = None

        # If note n_semitonesFromTonic is not the 7th in the current chord:
        # - keep an unaltered version
        # - create a new version by removing the 7th from the chord and doubling the root or the fifth
        
        if chord[3] != n:
            chord_no7th = copy.deepcopy(chord)
            # Remove last element (the 7th) from semitones list
            popped_note = chord_no7th.pop()
            
        # Else, note n_semitonesFromTonic is the 7th in the chord (no notes are removed)
        else:
            chord_no7th = None
            popped_note = None


        chord_inversions = []
        for inversion in [0, 1, 2, 3]:
            chord_inversions.append(self._handle_7th_inversions(chord, inversion))
    
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
        # Voice mapping for chord selection
        voice_mapping = {
            "Bass": 0,
            "Tenor": 1,
            "Alto": 2,
            "Soprano": 3
        }
        
        # Choose chord info dictionary based on key signature
        key_chord_info = MAJOR_KEY_CHORD_INFO if str(self.keySignature).split()[1] == "major" else MINOR_KEY_CHORD_INFO
        
        # Get diatonic notes in the scale of the key signature of the input melody
        s = self.keySignature.getScale()
        diatonic_notes = [str(p)[:-1] for p in scale.Scale.extractPitchList(s, comparisonAttribute="pitchClass")]
        
        # Check if melody note is diatonic
        n_noOctave = n.nameWithOctave[:-1]
        if n_noOctave in diatonic_notes:
            # Identify role of the note in the scale (+1 to get values in 1-7 instead of 0-6)
            degree = diatonic_notes.index(n_noOctave)+1
            
            n_semitonesFromTonic = key_chord_info[degree]["OffsetInSemitonesDegreeFromTonic"]
            
            # Get all diatonic chords where the note appears
            available_diatonic_chords = []
            for appearsIn in key_chord_info[degree]["AppearsInDegree"]:
                available_diatonic_chords.append(key_chord_info[appearsIn])
            

            print(f"Note: {n_noOctave}, degree: {degree}, n_semitonesFromTonic: {n_semitonesFromTonic}")
            print("Available chords:")
            for chord in available_diatonic_chords:
                print(chord)
            
            
            # Create all possible inversions
            available_chords = []
            for i in range(len(available_diatonic_chords)):
                curr_chord = copy.deepcopy(available_diatonic_chords[i]["SemitonesFromTonicSameOctave"])

                res = self._get_inversions(n_semitonesFromTonic, curr_chord)

                for r in res:
                    available_chords.append(r)
            
            
            # The following for loop:
            # 1. adjusts note's octaves so that the notes are in ascending order
            # 2. shifts all the notes so that the current note is transposed by 0 semitones (i.e. left unchanged) 
            # 3. if the chord spans more than two octaves, shifts the notes so that they fit in two octaves
            for i in range(len(available_chords)):
                curr_chord = available_chords[i]

                # 1.
                sorted = False
                while not sorted:
                    sorted = True
                    for i in range(len(curr_chord) - 1):
                        if curr_chord[i] >= curr_chord[i+1]:
                            curr_chord[i] -= 12
                            sorted = False
                
                # 2.
                for i in range(len(curr_chord)):
                    curr_chord[i] -= n_semitonesFromTonic

                # 3.
                if min(curr_chord) <= -12:
                    for i in range(len(curr_chord)):
                        curr_chord[i] += 12
                elif max(curr_chord) >= 12:
                    for i in range(len(curr_chord)):
                        curr_chord[i] -= 12

                # If note n appears only once in the chord as 12, traspose everything down by an octave
                if 0 not in curr_chord and 12 in curr_chord:
                    for i in range(len(curr_chord)):
                        curr_chord[i] -= 12
            
            # From chord list, only keep those where note n appears in the position corrisponding to the input melody voice
            # "[:]" syntax is to avoid list index skipping after removing an element from the list 
            for chord in available_chords[:]:
                correct_voice = voice_mapping[self.input_melody_voice]
                # 0 or 12 is number of semitones from note n, so n itself
                if chord[correct_voice] != 0 and chord[correct_voice] != 12:
                    available_chords.remove(chord)                    
            
            print("Final chord list after filtering:")
            for chord in available_chords:
                print(chord)
            print("\n")
            
            # Choose a random chord from those available
            chosen_chord = random.choice(available_chords)
            print(f"chosed_chord: {chosen_chord}")
            
            # Turn note list into tuple to ease unpacking
            return (*chosen_chord, )
            
            
        
        else:
            # COMPLETARE
            print(f"NON-DIATONIC: {n_noOctave}\n")
            return (None, None, None, None)
        

class EvoComposer:
    def __init__(self, melody_string, durations_string, generations=100, population_size=100, crossover_rate=0.7, mutation_rate=0.01):

        # Genetic algorithm stuff
        #self.population_size = population_size
        #self.crossover_rate = crossover_rate
        #self.mutation_rate = mutation_rate
        #self.generations = generations
        #self.population = []
        pass


    def _init_score(self):
        pass


    def initialize_population(self):
        """
        Initialize the population by building a chord on each note of the input melody.
        """
        pass


    def evaluate_fitness(self):
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
