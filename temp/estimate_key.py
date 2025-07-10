import music21
import numpy as np
import scipy.linalg

from constants import ENHARMONIC_KEYS

from scipy.stats import zscore
from dataclasses import dataclass


@dataclass
class KeyEstimator:
    """
    Implements the Krumhansl-Schmuckler algorithm to find the key of a melody.
    This function analyzes the melody stream and returns the most likely key based on the Krumhansl-Schmuckler algorithm.
    - For more information on the K-S algorithm, see:     https://rnhart.net/articles/key-finding/
    - For more information on the implementation, see:    https://www.youtube.com/watch?v=Dps2gSiFVbs
    - For calculation of improved key profile, see:       http://davidtemperley.com/wp-content/uploads/2015/11/temperley-mp99.pdf (uncomment lines labeled as (K-S) to use original K-S key profiles and calculations)
    
    Future work: impement the rest of the (Temperley, 1999) modifications to the Krumhansl-Schmuckler algorithm.
    
    Args:
        melody_stream (music21.stream.Stream): A music21 stream containing the melody notes.
        
    Returns:
        str: The estimated key of the melody.
    """
    
    # Define the (updated) Krumhansl-Schmuckler key profiles
    major = np.asarray([5, 2, 3.5, 2, 4.5, 4, 2, 4.5, 2, 3.5, 1.5, 4])
    minor = np.asarray([5, 2, 3.5, 4.5, 2, 4, 2, 4.5, 3.5, 2, 1.5, 4])
    
    # Define the (original) Krumhansl-Schmuckler key profiles
    #(K-S) major = np.asarray([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
    #(K-S) minor = np.asarray([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
    
    
    # Ran after the dataclass is initialized
    def __post_init__(self):        
        #(K-S) self.major = zscore(self.major)
        #(K-S) self.major_norm = np.linalg.norm(self.major)
        self.major = scipy.linalg.circulant(self.major)
    
        #(K-S) self.minor = zscore(self.minor)
        #(K-S) self.minor_norm = np.linalg.norm(self.minor)
        self.minor = scipy.linalg.circulant(self.minor)


    # Allows the class to be called like a function
    def __call__(self, melody_stream: music21.stream.Stream):
        melody_profile = self.get_melody_profile(melody_stream)
        
        # Normalize the melody profile and calcolate its norm
        #(K-S) melody_profile_norm = np.linalg.norm(melody_profile)
        
        # Calculate the correlation with major and minor profiles
        major_corr = np.dot(melody_profile, self.major) #(K-S) / (melody_profile_norm * self.major_norm)
        minor_corr = np.dot(melody_profile, self.minor) #(K-S) / (melody_profile_norm * self.minor_norm)
        ## Return both major and minor correlation coefficients
        #return major_corr, minor_corr
        
        
        ## Return only the most likely key
        # Create a mapping for the pitch classes to their names
        mapping = {0: "C", 1: "C#/D-", 2: "D", 3: "D#/E-", 4: "E", 5: "F", 6: "F#/G-", 7: "G", 8: "G#/A-", 9: "A", 10: "A#/B-", 11: "B"}
        
        # Calculate the most likely major and minor keys
        most_likely_major = mapping[np.argmax(major_corr)]
        most_likely_minor = mapping[np.argmax(minor_corr)]
        
        print(f"Most likely major: {most_likely_major} major_corr: {np.max(major_corr)}")
        print(f"Most likely minor: {most_likely_minor} minor_corr: {np.max(minor_corr)}")
        
        if np.max(major_corr) > np.max(minor_corr):
            most_likely_key = most_likely_major
        
        else: 
            most_likely_key = most_likely_minor.lower()


        # Choose between enharmonic equivalents (e.g. C# and D-) based on which one covers most notes of the melody
        if most_likely_key in ENHARMONIC_KEYS:
            # Separate key names
            key1_text, key2_text = most_likely_key.split(sep="/")
            
            #print(f"Deciding between {key1_text} and {key2_text}")
            
            # Create keySignatures to access altered pitches names
            keySignature1 = music21.key.KeySignature(music21.key.Key(key1_text).sharps)
            keySignature2 = music21.key.KeySignature(music21.key.Key(key2_text).sharps)
            
            
            count1 = count2 = 0
            for note in melody_stream.notes:            
                if note.name in [str(p) for p in keySignature1.alteredPitches]:
                    count1+=1
                elif note.name in [str(p) for p in keySignature2.alteredPitches]:
                    count2+=1

            most_likely_key = key1_text if count1 > count2 else key2_text
            

        #melody_stream.keySignature = music21.key.Key(most_likely_key)
        print("Key signature of the melody has been set to:", melody_stream.keySignature)
        

    def get_melody_profile(self, melody_stream: music21.stream.Stream) -> np.array:
        """
        Extracts the melody profile from the note durations in melody stream.
        
        Args:
            melody_stream (music21.stream.Stream): A music21 stream containing the melody notes.
        
        Returns:
            np.array: The melody profile as a numpy array.
        """
        
        # Initialize a profile for pitch classes (0-11)
        melody_profile = np.zeros(12)
        for note in melody_stream.notes:
            # Get the pitch class (0-11) and add the duration to the profile
            pitch = note.pitch.midi % 12
            melody_profile[pitch] += note.duration.quarterLength

        return zscore(melody_profile)




if __name__ == "__main__":
    from parse_input import createMelodyFromString

    # Example usage
    melody_string =     "r E5 F#5 G5 A5 F#5 D5 E5 E5 r"
    duration_string =   "2 0.5 0.5 0.5 0.5 1 0.5 0.5 1 1"
    melody_stream = createMelodyFromString(melody_string, duration_string)

    print(melody_stream.analyze("key"))
    print(music21.analysis.discrete.analyzeStream(melody_stream, "key"))
    melody_stream.show("midi")

    #key_estimator = KeyEstimator()
    #
    #key_estimator(melody_stream)
    #melody_stream.show("midi")
