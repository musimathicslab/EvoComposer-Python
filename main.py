from music21 import *
from utility.evo_composer import *


if __name__ == "__main__":
    #input_melody_string = "tinyNotation: 4/4 e'4 f' g' a' f'# d' e' e'"
    melody_str = "tinyNotation: 4/4 c'4 d' e' f#' g' a' b' c''"
    voice = "Soprano"
    
    melody = converter.parse(melody_str)
    
    print("EvoComposer setup")
    evc = EvoComposer(melody, voice, population_size=1)

    print("EvoComposer init")
    evc.initialize_population()
    
    for chrom in evc.population:
        print(chrom)
    
    print("EvoComposer evaluate")
    evc.evaluate()
    
    print("EvoComposer run generations")
    evc.run()
