from music21 import *

# Max number of notes in each beat
N = 16

class InputParser:
    """Creates score containing Soprano, Alto, Tenor and Bass parts with the specified number of measures, time signature and key signature and assigns input melody to the correct part.
    """
    def __init__(self, input_melody_string, input_melody_voice, n_measures, time_sig = "4/4"):
        # Time signature
        self.n_measures = n_measures
        self.time_sig = self._validate_time_sig(input_melody_string, time_sig)
        
        # "Numerator" of time signature
        self.n_beats = int(self.time_sig.split("/")[0])
        
        # "Denominator" of time signature
        self.note_value = int(self.time_sig.split("/")[1])


        # Simple grid to show composition layout
        self.grid = [
            [0] * (N*self.n_beats*self.n_measures),
            [0] * (N*self.n_beats*self.n_measures),
            [0] * (N*self.n_beats*self.n_measures),
            [0] * (N*self.n_beats*self.n_measures)
        ]
        
        # Create melody stream from input string
        self.input_melody_string = input_melody_string
        self.melody_stream = self._init_stream(self.input_melody_string)

        # Key signature
        self.keySignature = self.melody_stream.analyze("key")

        # Input melody voice
        self.input_melody_voice = input_melody_voice
        
        # Create score object
        self.score = self._init_score()
        
        # Fill grid
        self._fill_grid()

    
    def _init_stream(self, input_melody):
        """Converts input melody string to stream

        Args:
            input_melody (str): string containing space-separated note names (A to G) followed by alteration simbols ("#" for sharps and "-" for flats) and octave information (tipically from 2 to 6).

        Returns:
            stream.Stream: stream representation of input melody
        """
        melody_stream = stream.Stream()
        for n in input_melody.split():
            melody_stream.append(note.Note(n))
        
        return melody_stream
    
    
    def _init_score(self):
        """
        Create score rapresentation of melody and parts. The object contains four different Part objects for the Soprano, Alto, Tenor and Bass voices.
        Each part contains n_measures measures (with the first one containing the key signature and the time signature), each (implicitly) divided in n_beats beats.
        Each note must be a quarter note, which means that each measure contains n_beats notes (every note falls on-beat).
        
        Returns:
            stream.Score(): score object containing parts, measures and input melody.
        """
        score = stream.Score()
        
        # Part objects to represent single voice parts
        self.soprano = stream.Part()
        self.soprano.id = "Soprano"
        self.soprano.append(instrument.Instrument("Soprano"))
        
        self.alto = stream.Part()
        self.alto.id = "Alto"
        self.alto.append(instrument.Instrument("Alto"))
        
        self.tenor = stream.Part()
        self.tenor.id = "Tenor"
        self.tenor.append(instrument.Instrument("Tenor"))

        self.bass = stream.Part()
        self.bass.id = "Bass"
        self.bass.append(instrument.Instrument("Bass"))

        # Add parts to Score object
        score.append([self.soprano, self.alto, self.tenor, self.bass])
        
        
        ## Add specified number of measures to each part        
        # For each measure
        for i in range(1, self.n_measures+1):
            # For each part
            for p in score.parts:
                # Create the measure
                m = stream.Measure(number=i)

                # Add time signature and key signature to first measure of each part
                if i == 1:
                    m.append(meter.TimeSignature(self.time_sig))     
                    m.append(self.melody_stream.analyze("key"))
                
                # Insert measure in part at the correct offset (that is, measure index * measure length in number of beats)
                p.insert(offsetOrItemOrList=(i * self.n_beats), itemOrNone=m)
        
        ## Add melody to correct part
        # For each part in the score
        for p in score.parts:
            # For the specified part
            if p.partName == self.input_melody_voice:
                # Iterate over the length of each measure
                for i in range(1, self.n_beats+1):
                    # Select the notes that are supposed to go in the i-th measure
                    notes = self.melody_stream.notes[(i-1)*self.n_beats: (i-1)*self.n_beats+self.n_beats]
                    m = p.measure(i)
                    # Add the notes to said measure
                    for n in notes:
                        m.append(n)
            
                break

        return score
        
    
    def _validate_time_sig(self, input_melody_string, time_sig):
        """Checks if input time signature is valid and if it's consistent with the number of notes in the input melody.

        Args:
            input_melody_string (str): string representation of the melody
            time_sig (str): str representing the time signature in the form "a/b" where "a" is the number of beats in each measure and "b" is the note value (must be 4).

        Raises:
            ValueError: raised if b is not equal to 4 or if there are too few/many notes in the input string which makes it so that notes cannot be used to fill specified number of measures.

        Returns:
            str: time_sig received as input
            str: numerator of time_sig
        """

        # "Numerator" of time signature
        n_beats = int(time_sig.split("/")[0])
        
        # "Denominator" of time signature
        note_value = int(time_sig.split("/")[1])
        
        # Number of notes in melody
        n_notes = len(input_melody_string.split())
        
        # If "denominator" is equal to 4
        if note_value == 4:
            # If there are enough notes (quarter notes by default) to fill all beats in all measures
            if n_notes == n_beats * self.n_measures:
                return time_sig
            else:
                raise ValueError("Too many or too few notes for specified number of measures and time signature.")
        else:
            raise ValueError("Note value (denominator of time signature) must equal to 4.")
    
    
    def _fill_grid(self):
        """Simple representation of the score to verify correct handling of notes and beats
        """
        notes = self.input_melody_string.split()

        # Iterate over voices
        for i in range(len(self.grid)):
            # Iterate over notes
            for j in range(len(notes)):
                # Insert notes "on-beat"
                self.grid[i][j * N] = notes[j]
                
    
    def print_grid(self):
        for row in self.grid:
            print(row)