import music21
from utility.get_voice import get_voice
from utility.parse_input import createMelodyFromString

class EvoComposer:
    def __init__(self, melody_string, duration_string, generations=100, population_size=100, crossover_rate=0.7, mutation_rate=0.01):
        self.melody_stream = createMelodyFromString(melody_string, duration_string)

        # Estimate key of the input melody
        #self.melody_stream.keySignature = self.melody_stream.analyze("key")

        # Identify which part plays the input melody
        # SISTEMARE: invece che usare una variabile diversa, modificare get_voice in modo che setti la voice della melodia come suo attributo (se esistente, altrimenti viene creato), come è stato fatto per la key
        # CAMBIO DI PIANI: questo verrà fatto una volta creato lo score con le varie parti che formano gli accordi
        self.input_melody_voice = get_voice(self.melody_stream)
        
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.population = []


    def initialize_population(self):
        """
        Initialize the population by building a chord on each note of the input melody.
        """
        pass


    def evaluate_fitness(self):
        # Evaluate the fitness of each individual in the population
        pass


    def select_parents(self):
        # Select parents based on their fitness for reproduction
        pass


    def crossover(self, parent1, parent2):
        # Perform crossover between two parents to create offspring
        pass


    def mutate(self, individual):
        # Mutate an individual with a certain probability
        pass


    def run(self):
        # Run the evolutionary algorithm for a specified number of generations
        pass





if __name__ == "__main__":
    # Example usage
    #melody_string =     "F#5 F#5 G3 A4 F4 B-5 C4 F3 F4 E5"
    #duration_string =   "4 1 1 1 1 1 1 1 0.5 0.5"
    melody_string =     "r E5 F#5 G5 A5 F#5 D5 E5 E5 r"
    duration_string =   "2 0.5 0.5 0.5 0.5 1 0.5 0.5 1 1"
    
    evc = EvoComposer(melody_string, duration_string)
    
    print(f"Melody: {[str(p) for p in evc.melody_stream.pitches]}")
    print(f"Key: {evc.melody_stream.keySignature}")
    print(f"Voice: {evc.input_melody_voice}")
    evc.melody_stream.show()