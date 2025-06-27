#import music21
#
#def build_chord(note, key):
#    if note in key.


if __name__ == "__main__":
    from parse_input import createMelodyFromString

    # Example usage
    melody_string = "F5 F5 G3 A4 F4 B5 C4 F3 F4 E5"
    duration_string = "4 1 1 1 1 1 1 1 0.5 0.5"
    melody_stream = createMelodyFromString(melody_string, duration_string)
    
    print(melody_stream.keySignature)