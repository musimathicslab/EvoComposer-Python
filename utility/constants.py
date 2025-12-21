# Key of the dictionary is the degree of each note in the scale
MAJOR_KEY_CHORD_INFO = {
    1: {
        "Type": ["maj", "maj7th"],
        "OffsetInSemitonesDegreeFromTonic": 0,
        "SemitonesFromTonicSameOctave": [0, 4, 7, 11],
        "SemitonesFromTonicDifferentOctave": [0, 4, 7, 11],
        "SemitonesFromLastNote": [0, 4, 3, 4],
        "AppearsInDegree": [1, 2, 4, 5]
    },
    
    2: {
        "Type": ["min", "min7th"],
        "OffsetInSemitonesDegreeFromTonic": 2,
        "SemitonesFromTonicSameOctave": [2, 5, 9, 0],
        "SemitonesFromTonicDifferentOctave": [2, 5, 9, 12],
        "SemitonesFromLastNote": [0, 3, 4, 3],
        "AppearsInDegree" : [2, 3, 5, 7]
    },
    
    3: {
        "Type": ["min", "min7th"],
        "OffsetInSemitonesDegreeFromTonic": 4,
        "SemitonesFromTonicSameOctave": [4, 7, 11, 2],
        "SemitonesFromTonicDifferentOctave": [4, 7, 11, 14],
        "SemitonesFromLastNote": [0, 4, 3, 4],
        "AppearsInDegree": [1, 3, 4, 6]
    },
    
    4: {
        "Type": ["maj", "maj7th"],
        "OffsetInSemitonesDegreeFromTonic": 5,
        "SemitonesFromTonicSameOctave": [5, 9, 0, 4],
        "SemitonesFromTonicDifferentOctave": [5, 9, 12, 16],
        "SemitonesFromLastNote": [0, 4, 3, 4],
        "AppearsInDegree": [2, 4, 5, 7]
    },
    
    5: {
        "Type": ["maj", "dom7th"],
        "OffsetInSemitonesDegreeFromTonic": 7,
        "SemitonesFromTonicSameOctave": [7, 11, 2, 5],
        "SemitonesFromTonicDifferentOctave": [7, 11, 14, 17],
        "SemitonesFromLastNote": [0, 4, 3, 3],
        "AppearsInDegree": [1, 3, 5, 6]
    },
    
    6: {
        "Type": ["min", "min7th"],
        "OffsetInSemitonesDegreeFromTonic": 9,
        "SemitonesFromTonicSameOctave": [9, 0, 4, 7],
        "SemitonesFromTonicDifferentOctave": [9, 12, 16, 19],
        "SemitonesFromLastNote": [0, 3, 4, 3],
        "AppearsInDegree": [2, 4, 6, 7]
    },
    
    7: {
        "Type": ["dim", "halfdim7th"],
        "OffsetInSemitonesDegreeFromTonic": 11,
        "SemitonesFromTonicSameOctave": [11, 2, 5, 9],
        "SemitonesFromTonicDifferentOctave": [11, 14, 17, 21],
        "SemitonesFromLastNote": [0, 3, 3, 4],
        "AppearsInDegree": [1, 3, 5, 7]
    }
}


MINOR_KEY_CHORD_INFO = {
    1: {
        "Type": ["min", "min7th"],
        "OffsetInSemitonesDegreeFromTonic": 0,
        "SemitonesFromTonicSameOctave": [0, 3, 7, 10],
        "SemitonesFromTonicDifferentOctave": [0, 3, 7, 10],
        "SemitonesFromLastNote": [0, 3, 4, 3],
        "AppearsInDegree": [1, 2, 4, 6]
    },
    
    2: {
        "Type": ["dim", "halfdim7th"],
        "OffsetInSemitonesDegreeFromTonic": 2,
        "SemitonesFromTonicSameOctave": [2, 5, 8, 0],
        "SemitonesFromTonicDifferentOctave": [2, 5, 8, 12],
        "SemitonesFromLastNote": [0, 3, 3, 4],
        "AppearsInDegree": [2, 3, 5, 7]
    },
    
    3: {
        "Type": ["maj", "maj7th"],
        "OffsetInSemitonesDegreeFromTonic": 3,
        "SemitonesFromTonicSameOctave": [3, 7, 10, 2],
        "SemitonesFromTonicDifferentOctave": [3, 7, 10, 14],
        "SemitonesFromLastNote": [0, 4, 3, 4],
        "AppearsInDegree": [1, 3, 4, 6]
    },
    
    4: {
        "Type": ["min", "min7th"],
        "OffsetInSemitonesDegreeFromTonic": 5,
        "SemitonesFromTonicSameOctave": [5, 8, 0, 3],
        "SemitonesFromTonicDifferentOctave": [5, 8, 12, 15],
        "SemitonesFromLastNote": [0, 3, 4, 3],
        "AppearsInDegree": [2, 4, 5, 7]
    },
    
    5: {
        "Type": ["min", "min7th"],
        "OffsetInSemitonesDegreeFromTonic": 7,
        "SemitonesFromTonicSameOctave": [7, 10, 2, 5],
        "SemitonesFromTonicDifferentOctave": [7, 10, 14, 17],
        "SemitonesFromLastNote": [0, 3, 4, 3],
        "AppearsInDegree": [1, 2, 4, 6]
    },
    
    6: {
        "Type": ["maj", "maj7th"],
        "OffsetInSemitonesDegreeFromTonic": 8,
        "SemitonesFromTonicSameOctave": [8, 0, 3, 7],
        "SemitonesFromTonicDifferentOctave": [8, 12, 15, 19],
        "SemitonesFromLastNote": [0, 4, 3, 4],
        "AppearsInDegree": [2, 4, 6, 7]
    },
    
    7: {
        "Type": ["maj", "dom7th"],
        "OffsetInSemitonesDegreeFromTonic": 10,
        "SemitonesFromTonicSameOctave": [10, 2, 5, 8],
        "SemitonesFromTonicDifferentOctave": [10, 14, 17, 20],
        "SemitonesFromLastNote": [0, 4, 3, 3],
        "AppearsInDegree": [1, 3, 5, 7]
    }    
}

# Key signatures
KEY_SIGNATURES = [
        "C major", "C# major", "D- major", "D major", "D# major", "E- major", "E major", "F major", "F# major", "G- major", "G major", "G# major", "A- major", "A major", "A# major", "B- major", "B major",
        "c minor", "c# minor", "d- minor", "d minor", "d# minor", "e- minor", "e minor", "f minor", "f# minor", "g- minor", "g minor", "g# minor", "a- minor", "a minor", "a# minor", "b- minor", "b minor",
    ]

# Notes
NOTES = ["C", "C#", "D-", "D", "D#", "E-", "E", "F", "F#", "G-", "G", "G#", "A-", "A", "A#", "B-", "B"]
    

# Harmonic weights
WEIGHTS_SAME_MAJOR_TONALITY = {
    "I":        {"I": 0.226, "ii": 0.025, "iii": 0.025, "IV": 0.266, "V": 0.266, "vi": 0.150, "vii°": 0.002},
    "ii":       {"I": 0.025, "ii": 0.400, "iii": 0.025, "IV": 0.075, "V": 0.400, "vi": 0.075, "vii°": 0},
    "iii":      {"I": 0.016, "ii": 0.016, "iii": 0.400, "IV": 0.150, "V": 0.016, "vi": 0.400, "vii°": 0.002},
    "IV":       {"I": 0.075, "ii": 0.075, "iii": 0.025, "IV": 0.400, "V": 0.400, "vi": 0.025, "vii°": 0},
    "V":        {"I": 0.400, "ii": 0.025, "iii": 0.025, "IV": 0.075, "V": 0.400, "vi": 0.075, "vii°": 0},
    "vi":       {"I": 0.050, "ii": 0.266, "iii": 0.075, "IV": 0.075, "V": 0.266, "vi": 0.266, "vii°": 0.002},
    "vii°":     {"I": 0.226, "ii": 0.025, "iii": 0.025, "IV": 0.266, "V": 0.266, "vi": 0.150, "vii°": 0.002}
}

WEIGHTS_SAME_MINOR_TONALITY = {
    "i":        {"i": 0.226, "ii°": 0.016, "III": 0.016, "iv": 0.266, "V": 0.266, "VI": 0.150, "vii°": 0.016, "VII": 0},
    "ii°":      {"i": 0.025, "ii°": 0.400, "III": 0.025, "iv": 0.075, "V": 0.400, "VI": 0.075, "vii°": 0, "VII": 0},
    "III":      {"i": 0.012, "ii°": 0.012, "III": 0.400, "iv": 0.150, "V": 0.120, "VI": 0.400, "vii°": 0, "VII": 0.120},
    "iv":       {"i": 0.075, "ii°": 0.075, "III": 0.025, "iv": 0.400, "V": 0.400, "VI": 0.025, "vii°": 0, "VII": 0},
    "V":        {"i": 0.400, "ii°": 0.025, "III": 0.025, "iv": 0.075, "V": 0.400, "VI": 0.075, "vii°": 0, "VII": 0},
    "vi":       {"i": 0.050, "ii°": 0.266, "III": 0.075, "iv": 0.075, "V": 0.266, "VI": 0.266, "vii°": 0, "VII": 0},
    "vii°":     {"i": 0.950, "ii°": 0, "III": 0, "iv": 0, "V": 0, "VI": 0, "vii°": 0.050, "VII": 0},
    "VII":      {"i": 0, "ii°": 0, "III": 0.400, "iv": 0.050, "V": 0, "VI": 0.150, "vii°": 0, "VII": 0.400}
}

# Harmonic coefficients