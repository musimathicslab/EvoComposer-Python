from music21 import *
from utility.evo_composer import *


if __name__ == "__main__":
    input_melody_string = "tinyNotation: 4/4 e'4 f' g' a' f'# d' e' e'"
    input_melody_voice = "Soprano"
    
    # Note retrieval test
    """
    obj = Chromosome(converter.parse(input_melody_string), input_melody_voice)
    parts = obj.score.getElementsByClass(stream.Part)
    for part in parts:
        print(f"Part: {part.id}")
        measures = part.getElementsByClass(stream.Measure)
        
        for measure in part:
            print(f"Measure at offset: {measure.offset}")
            notes = measure.getElementsByClass(note.Note)
            [print(n) for n in notes]
        print()
    """
    
    # initialize_population test
    """
    evc = EvoComposer(input_melody_string, input_melody_voice)
    i=0
    for c in evc.population:
        i+=1
        print(f"{i}) {c.score}")
    """
    