from music21 import *
from utility.evo_composer import *


if __name__ == "__main__":
    #input_melody_string = "tinyNotation: 4/4 e'4 f' g' a' f'# d' e' e'"
    input_melody_string = "tinyNotation: 4/4 c'4 d' e' f#' g' a' b' c''"
    input_melody_voice = "Soprano"
    
    evc = EvoComposer(input_melody_string, input_melody_voice, p_size=1)
    
    for chrom in evc.population:
        print(chrom)
    
    print("Evaluating...")
    evc.evaluate()