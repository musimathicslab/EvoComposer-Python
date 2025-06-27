from .constants import BASS_RANGE, TENOR_RANGE, ALTO_RANGE, SOPRANO_RANGE

def get_voice(melody_stream):
    """
    Identifies which voice is the one that most likely plays the input melody based on its range. As the melody is usually played by the highest voice because it's the one who's frequency the human ear is most sensitive to,
    voices are given priority from higheset to lowest.
    The range of the melody is evaluated and a label is returned based on witch voice range it overlaps with the most (giving priority from highest to lowest).
    
    Args:
        melody_stream (music21.stream.Stream): A music21 stream containing the melody notes.
    
    Returns:
        str: A label indicating the voice range in which the melody fits best.
    """

    voices = {"Soprano": 0, "Alto": 0, "Tenor": 0, "Bass": 0}

    for note in melody_stream.notes:
        if note.nameWithOctave in SOPRANO_RANGE:
            voices["Soprano"] += 1
            
        if note.nameWithOctave in ALTO_RANGE:
            voices["Alto"] += 1
        
        if note.nameWithOctave in TENOR_RANGE:
            voices["Tenor"] += 1

        if note.nameWithOctave in BASS_RANGE:
            voices["Bass"] += 1
    
    return max(voices, key=voices.get)



if __name__ == "__main__":
    from parse_input import createMelodyFromString

    # Example usage
    melody_string = "F5 F5 G3 A4 F4 B5 C4 F3 F4 E5"
    duration_string = "4 1 1 1 1 1 1 1 0.5 0.5"
    melody_stream = createMelodyFromString(melody_string, duration_string)

    voice = get_voice(melody_stream)
    print(voice)