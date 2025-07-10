from music21 import *

CHORD_TYPES = {
    "major": [],
    "minor": [],
    "major7th": [],
    "minor7th": [],
    "dominanth7th": [],
    "halfdim7th": [],
}

class Chromosome:
    """In the context, a chromosome is a certain harmonization built of the input melody that has either been built
    while initializing the population or obtained by crossover/mutation during the algorithm's epochs.
    """
    def __init__(self, parsed_input):
        # InputParser object, containing all the useful attrbutes
        self.parsed_input = parsed_input
        
    
    def _build_chord(self, note):
        pass
        

class EvoComposer:
    def __init__(self, melody_string, durations_string, generations=100, population_size=100, crossover_rate=0.7, mutation_rate=0.01):

        # Genetic algorithm stuff
        #self.population_size = population_size
        #self.crossover_rate = crossover_rate
        #self.mutation_rate = mutation_rate
        #self.generations = generations
        #self.population = []
        pass


    def _init_score(self):
        pass


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
