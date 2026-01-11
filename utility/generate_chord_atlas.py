from music21 import *
import os
import copy
import json
from constants import MAJOR_KEY_CHORD_INFO, MINOR_KEY_CHORD_INFO, KEY_SIGNATURES, NOTES

def _handle_7th_inversions(curr_chord, inv):
    before_inv = copy.deepcopy(curr_chord)
    
    # Invert voicing
    after_inv = before_inv[inv:] + before_inv[:inv]
    return after_inv


def _handle_triad_inversions(curr_chord, inv):
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


def get_inversions(n, curr_chord):
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
        chord_inversions.append(_handle_7th_inversions(curr_chord, inversion))

    if chord_no7th:
        for inversion in [0, 1, 2]:
            inv1, inv2 = _handle_triad_inversions(chord_no7th, inversion)
            
            if inv2:
                chord_inversions.append(inv1)
                chord_inversions.append(inv2)
            else:
                chord_inversions.append(inv1)
    
    return chord_inversions


def generate_chord_atlas():
    """Creates a json file where each key is a key signature and each value is a list of all diatonic chords for that key
    """
    
    chord_atlases_path = "./chord_atlases"
    if not os.path.exists(chord_atlases_path):
        os.makedirs(chord_atlases_path)

    # Dictionary to be dumped in a json file
    chord_atlas = {}
    
    

    # For each key signature
    for key_signature in KEY_SIGNATURES:        
        key_tonic = key_signature.split()[0]
        key_mode = key_signature.split()[1]

        k = key.Key(key_tonic, key_mode)

        # Choose chord info dictionary based on key signature
        key_chord_info = MAJOR_KEY_CHORD_INFO if key_mode == "major" else MINOR_KEY_CHORD_INFO

        s = k.getScale(k.mode)
        diatonic_notes = [str(p)[:-1] for p in scale.Scale.extractPitchList(s, comparisonAttribute="pitchClass")]
        
        diatonic_chords = {}
        # For each note in the scale
        for n in diatonic_notes:
            
            # Identify role of the note in the scale (+1 to get values in 1-7 instead of 0-6)
            degree = diatonic_notes.index(n)+1
            
            n_semitonesFromTonic = key_chord_info[degree]["OffsetInSemitonesDegreeFromTonic"]
                
            # Get all diatonic chords where the note appears
            available_diatonic_chords = []
            for appearsIn in key_chord_info[degree]["AppearsInDegree"]:
                available_diatonic_chords.append(key_chord_info[appearsIn])
            
            # Create all possible inversions
            available_chords = []
            for i in range(len(available_diatonic_chords)):
                curr_chord = copy.deepcopy(available_diatonic_chords[i]["SemitonesFromTonicSameOctave"])

                res = get_inversions(n_semitonesFromTonic, curr_chord)

                for r in res:
                    available_chords.append(r)
                
                # The following for loop:
                # 1. adjusts note's octaves so that the notes are in ascending order
                # 2. if the chord spans more than two octaves, shifts the notes so that they fit in two octaves
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
                    if min(curr_chord) <= -12:
                        for i in range(len(curr_chord)):
                            curr_chord[i] += 12
                    elif max(curr_chord) >= 12:
                        for i in range(len(curr_chord)):
                            curr_chord[i] -= 12

            diatonic_chords[n] = available_chords
        
        chord_atlas[key_signature] = diatonic_chords

    # Dump chord atlas in json file
    with open(os.path.join(chord_atlases_path, "keys_chord_atlas.json"), "w") as f:
        json.dump(chord_atlas, f, indent=3, separators=(',', ': '))


def generate_note_chord_atlas():
    """Creates a json file where each note is a key signatures and each value is a lists of all diatonic chords, for that key, that contain that note
    """
    
    # Create folder
    chord_atlases_path = ".\\chord_atlases"
    if not os.path.exists(chord_atlases_path):
        os.makedirs(chord_atlases_path)
        
    
    with open(os.path.join(chord_atlases_path, 'keys_chord_atlas.json'), 'r') as file:
        chord_atlas = json.load(file)

    for n in NOTES:
        n_chord_atlas = {}

        # For each key signature 
        for key_signature in chord_atlas.keys():
            n_chord_atlas[key_signature] = []
            
            key_tonic = key_signature.split()[0]
            key_mode = key_signature.split()[1]

            k = key.Key(key_tonic, key_mode)

            key_chord_info = MAJOR_KEY_CHORD_INFO if key_mode == "major" else MINOR_KEY_CHORD_INFO
            
            # Get diatonic notes
            s = k.getScale(k.mode)
            diatonic_notes = [str(p)[:-1] for p in scale.Scale.extractPitchList(s, comparisonAttribute="pitchClass")]

            # If n is diatonic, get all chords where it appears
            if n in diatonic_notes:
                # Get role of note n in current key signature
                n_degree = diatonic_notes.index(n)+1
                n_semitonesFromTonic = key_chord_info[n_degree]["OffsetInSemitonesDegreeFromTonic"]
                #print(f"Note: {n}, degree: {n_degree}, key: {key_signature}, n_semitonesFromTonic: {[n_semitonesFromTonic-12, n_semitonesFromTonic, n_semitonesFromTonic+12]}")
                
                for degree in chord_atlas[key_signature].keys():
                    for curr_chord in chord_atlas[key_signature][degree]:
                        if n_semitonesFromTonic in curr_chord or str(n_semitonesFromTonic-12) in curr_chord or str(n_semitonesFromTonic+12) in curr_chord:
                            c = copy.deepcopy(curr_chord)
                            
                            # Shift all the notes so that the current note is transposed by 0 semitones (i.e. left unchanged) 
                            for i in range(len(c)):
                                c[i] -= n_semitonesFromTonic

                            # Make it so the original note, i.e. the 0-semitones transposition, is always present
                            if 0 not in c:
                                if 12 in c:
                                    for i in range(len(c)):
                                        c[i] -= 12
                                elif -12 in c:
                                    for i in range(len(c)):
                                        c[i] += 12
                            
                            if c not in n_chord_atlas[key_signature]:
                                n_chord_atlas[key_signature].append(c)
        
        with open(os.path.join(chord_atlases_path, n + "_chord_atlas.json"), 'w') as f:
            json.dump(n_chord_atlas, f, indent=3, separators=(',', ': '))


if __name__ == "__main__":
    generate_chord_atlas()
    generate_note_chord_atlas()