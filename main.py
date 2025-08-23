from music21 import *
from utility.evo_composer import *


if __name__ == "__main__":
    input_melody_string = "tinyNotation: 4/4 e'8 f' g' a' f'#4 d'8 e'~ e'"
    input_melody_voice = "Soprano"
    
    obj = Chromosome(input_melody_string, input_melody_voice)
    