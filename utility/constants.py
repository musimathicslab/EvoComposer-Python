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
        "Type": ["min", "minmaj7th"],
        "OffsetInSemitonesDegreeFromTonic": 0,
        "SemitonesFromTonicSameOctave": [0, 3, 7, 11],
        "SemitonesFromTonicDifferentOctave": [0, 3, 7, 11],
        "SemitonesFromLastNote": [0, 3, 4, 4],
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
        "Type": ["aug", "augmaj7th"],
        "OffsetInSemitonesDegreeFromTonic": 3,
        "SemitonesFromTonicSameOctave": [3, 7, 11, 2],
        "SemitonesFromTonicDifferentOctave": [3, 7, 11, 14],
        "SemitonesFromLastNote": [0, 4, 4, 3],
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

    ## Minor v not commonly used
    # 5: {
    #     "Type": ["min", "min7th"],
    #     "OffsetInSemitonesDegreeFromTonic": 7,
    #     "SemitonesFromTonicSameOctave": [7, 10, 2, 5],
    #     "SemitonesFromTonicDifferentOctave": [7, 10, 14, 17],
    #     "SemitonesFromLastNote": [0, 3, 4, 3],
    #     "AppearsInDegree": [1, 2, 4, 6]
    # },
    
    5: {
        "Type": ["maj", "dom7th"],
        "OffsetInSemitonesDegreeFromTonic": 7,
        "SemitonesFromTonicSameOctave": [7, 11, 2, 5],
        "SemitonesFromTonicDifferentOctave": [7, 11, 14, 17],
        "SemitonesFromLastNote": [0, 4, 3, 3],
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
        "Type": ["dim", "dim7th"],
        "OffsetInSemitonesDegreeFromTonic": 11,
        "SemitonesFromTonicSameOctave": [11, 2, 5, 8],
        "SemitonesFromTonicDifferentOctave": [11, 14, 17, 20],
        "SemitonesFromLastNote": [0, 3, 3, 3],
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
    "I":        {"I": 0.226, "ii": 0.025, "iii": 0.025, "IV": 0.266, "V": 0.266, "vi": 0.150, "vii": 0.002},
    "ii":       {"I": 0.025, "ii": 0.400, "iii": 0.025, "IV": 0.075, "V": 0.400, "vi": 0.075, "vii": 0},
    "iii":      {"I": 0.016, "ii": 0.016, "iii": 0.400, "IV": 0.150, "V": 0.016, "vi": 0.400, "vii": 0.002},
    "IV":       {"I": 0.075, "ii": 0.075, "iii": 0.025, "IV": 0.400, "V": 0.400, "vi": 0.025, "vii": 0},
    "V":        {"I": 0.400, "ii": 0.025, "iii": 0.025, "IV": 0.075, "V": 0.400, "vi": 0.075, "vii": 0},
    "vi":       {"I": 0.050, "ii": 0.266, "iii": 0.075, "IV": 0.075, "V": 0.266, "vi": 0.266, "vii": 0.002},
    "vii":      {"I": 0.226, "ii": 0.025, "iii": 0.025, "IV": 0.266, "V": 0.266, "vi": 0.150, "vii": 0.002}
}

WEIGHTS_SAME_MINOR_TONALITY = {
    "i":        {"i": 0.226, "ii": 0.016, "III": 0.016, "iv": 0.266, "V": 0.266, "VI": 0.150, "vii": 0.016, "VII": 0},
    "ii":       {"i": 0.025, "ii": 0.400, "III": 0.025, "iv": 0.075, "V": 0.400, "VI": 0.075, "vii": 0,     "VII": 0},
    "III":      {"i": 0.012, "ii": 0.012, "III": 0.400, "iv": 0.150, "V": 0.120, "VI": 0.400, "vii": 0,     "VII": 0.120},
    "iv":       {"i": 0.075, "ii": 0.075, "III": 0.025, "iv": 0.400, "V": 0.400, "VI": 0.025, "vii": 0,     "VII": 0},
    "V":        {"i": 0.400, "ii": 0.025, "III": 0.025, "iv": 0.075, "V": 0.400, "VI": 0.075, "vii": 0,     "VII": 0},
    "VI":       {"i": 0.050, "ii": 0.266, "III": 0.075, "iv": 0.075, "V": 0.266, "VI": 0.266, "vii": 0,     "VII": 0},
    "vii":      {"i": 0.950, "ii": 0,     "III": 0,     "iv": 0,     "V": 0,     "VI": 0,     "vii": 0.050, "VII": 0},
    "VII":      {"i": 0,     "ii": 0,     "III": 0.400, "iv": 0.050, "V": 0,     "VI": 0.150, "vii": 0,     "VII": 0.400}
}

# Harmonic coefficients
COEFFICIENTS_SAME_MAJOR_TONALITY = {
    "I":        {"I": 8.1,  "ii": 2.5, "iii": 0.5, "IV": 0.7, "V": 18.5, "vi": 1.7, "vii": 0.3},
    "ii":       {"I": 0.9,  "ii": 0.6, "iii": 0.4, "IV": 0.2, "V": 10.4, "vi": 0.2, "vii": 0.2},
    "iii":      {"I": 0.9,  "ii": 0.3, "iii": 0.6, "IV": 0.5, "V": 0.8,  "vi": 0.6, "vii": 0.1},
    "IV":       {"I": 0.6,  "ii": 0.5, "iii": 0.1, "IV": 0.3, "V": 5.3,  "vi": 0.1, "vii": 0.2},
    "V":        {"I": 22.5, "ii": 0.6, "iii": 1.5, "IV": 0.8, "V": 10.8, "vi": 2.0, "vii": 0.1},
    "vi":       {"I": 0.4,  "ii": 0.6, "iii": 0.6, "IV": 0.4, "V": 2.2,  "vi": 0.7, "vii": 0.1},
    "vii":      {"I": 0.3,  "ii": 0.0, "iii": 0.0, "IV": 0.1, "V": 0.1,  "vi": 0.1, "vii": 0.1}
}

COEFFICIENTS_SAME_MINOR_TONALITY = {
    "i":        {"i": 17.1, "ii": 0.7, "III": 1.4, "iv": 6.4, "V": 15.6, "VI": 1.4, "vii": 2.1, "VII": 1.4},
    "ii":       {"i": 0.0,  "ii": 0.0, "III": 0.0, "iv": 0.0, "V": 3.3,  "VI": 0.0, "vii": 0.0, "VII": 0.0},
    "III":      {"i": 0.0,  "ii": 0.0, "III": 0.0, "iv": 0.0, "V": 0.0,  "VI": 0.0, "vii": 0.0, "VII": 0.0},
    "iv":       {"i": 2.3,  "ii": 0.2, "III": 0.2, "iv": 1.4, "V": 9.5,  "VI": 0.4, "vii": 0.3, "VII": 0.3},
    "V":        {"i": 22.6, "ii": 0.0, "III": 0.0, "iv": 0.8, "V": 8.0,  "VI": 0.0, "vii": 0.0, "VII": 0.1},
    "VI":       {"i": 0.0,  "ii": 0.0, "III": 0.0, "iv": 0.0, "V": 0.0,  "VI": 0.0, "vii": 0.0, "VII": 0.0},
    "vii":      {"i": 0.5,  "ii": 0.1, "III": 0.1, "iv": 0.2, "V": 0.4,  "VI": 0.0, "vii": 0.0, "VII": 0.0},
    "VII":      {"i": 1.1,  "ii": 0.0, "III": 0.0, "iv": 0.0, "V": 0.2,  "VI": 0.0, "vii": 0.0, "VII": 0.0}
}

COEFFICIENTS_MODULATION = {
    "C major":  {"D major": 0.1, "F major": 2.95, "G major": 4.6, "A major": 0.1, "a minor": 1.48},
    "D major":  {"G major": 3.2, "A major": 2.4, "b minor": 1.15},
    "D# major": {"A# major": 1.85},
    "E major":  {"A major": 1.9},
    "F major":  {"A# major": 2.7},
    "F# major": {"C major": 2.4, "d minor": 1.1},
    "G major":  {"C major": 4.5, "D major": 2.9, "e minor": 1.65},
    "G# major": {"A minor": 1.2},
    "A major":  {"D major": 2.87, "a minor": 1.2},
    "A# major": {"F major": 2.5, "g minor": 1.6},
    "B major":  {"D# major": 1.9},
    "e minor":  {"G major": 1.7},
    "g minor":  {"A# major": 1.4},
    "a minor":  {"C major": 1.5},
    "b minor":  {"D major": 1}
}