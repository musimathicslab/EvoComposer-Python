from music21 import *
from utility.parse_input import InputParser


if __name__ == "__main__":
    time_sig = "4/4"
    n_measures = 4
    
    input_melody_string = "4/4 e'8 f'# g' a' f'#4 d'8 e'~ e'"
    input_melody_voice = "Soprano"
    
    obj = InputParser(input_melody_string, input_melody_voice, n_measures, time_sig)
    
    
    obj.score.show("text")
    #obj.score.show("midi")
    
    #print(obj.score.keySignature, type(obj.score.keySignature))
    
    
    
    obj2 = converter.parse(input_melody_string, format="tinyNotation")
    print(obj2, type(obj2))
    
    obj2.show("text")
    #obj2.show("midi")
    
    print(obj2.analyze("key"))