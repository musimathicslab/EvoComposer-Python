import music21 as m21

def createMelodyFromString(melody_string, duration_string):
    """
    Create a music21 Stream from a string representation of a melody.
    
    Args:
        melody_string (str): A string representation of a melody, e.g. "C4 D4 E4 F4 G4 A4 B4 C5". Divide notes with a whitespace and use "#" for sharps and "-" for flats, as per music21 convention.
        durations_string (str): A string representation of the duration of each note in melody_string, e.g. "1" is a quarter note, "0.5" is an eight note, "2" is a half note and so on.
        
    Returns:
        stream.Stream: A music21 Stream object representing the melody.
    """
    notes = melody_string.split()
    durations = duration_string.split()

    melody_stream = m21.stream.Stream()
    
    for n, d in zip(notes, durations):
        try:
            # Create note
            note = m21.note.Note(n)

            # Set note duration
            note.duration.quarterLength = float(d)
            
            # Add note to stream
            melody_stream.append(note)
        except m21.exceptions21.Music21Exception as e:
            print(f"Error processing note '{n}': {e}")
    
    return melody_stream


if __name__ == "__main__":
    # melody_string = "C4 D4 E4 F4 G4 A4 B4 C5"
    melody_string =     "F3 F3 G3 A3 F3 B3 C4 F3 F3 E3"
    duration_string =   "4 1 1 1 1 1 1 1 0.5 0.5"
    melody_stream = createMelodyFromString(melody_string, duration_string)
    
    # Show stream in a music21 viewer
    melody_stream.show('midi')