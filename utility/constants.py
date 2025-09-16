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