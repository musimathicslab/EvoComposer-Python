import music21

def createMelodyFromString(melody_string, duration_string):
    """
    Create a music21 Stream from a string representation of a melody.
    
    Args:
        melody_string (str): A string representation of a melody, e.g. "C4 D4 E4 F4 G4 A4 B4 C5":
            - Notes/rests are divided with a whitespace
            - "#" indicates sharps
            - "-" indicates flats
            - "r" indicates rests
        durations_string (str): A string representation of the duration of each note/rest in melody_string, e.g. "1" is a quarter note, "0.5" is an eight note, "2" is a half note and so on.
        
    Returns:
        stream.Stream: A music21 Stream object representing the melody.
    """
    notes = melody_string.split()
    durations = duration_string.split()

    melody_stream = music21.stream.Stream()
    
    for n, d in zip(notes, durations):
        try:
            # Create note/rest
            if n == "r":
                note = music21.note.Rest()
            
            else: 
                note = music21.note.Note(n)

            # Set note/rest duration
            note.duration.quarterLength = float(d)
            
            # Add object to stream
            melody_stream.append(note)
        
        except music21.exceptions21.Music21Exception as e:
            print(f"Error processing note '{n}': {e}")
    
    return melody_stream


if __name__ == "__main__":
    melody_string =     "E5 F#5 G5 A5 F#5 D5 E5"
    duration_string =   "0.5 0.5 0.5 0.5 1 0.5 4.5"
    melody_stream = createMelodyFromString(melody_string, duration_string)
    
    # Show stream in a music21 viewer

    melody_stream.show("midi")