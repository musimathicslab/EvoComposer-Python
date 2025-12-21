from music21 import *
from utility.chromosome import Chromosome

class EvoComposer:
    def __init__(self, line_string, line_voice, p_size=5, p_c=0.7, p_m=0.01, max_gen=100):
        # Create line stream from input TinyNotation string
        self.line = converter.parse(line_string)
        self.line_voice = line_voice
        
        # Population size
        self.p_size = p_size
        
        # Probability of crossover
        self.p_c = p_c
        
        # Probability of mutation
        self.p_m = p_m
        
        # Maximum number of generations
        self.max_gen = max_gen
        
        self.population = self.initialize_population()


    def initialize_population(self):
        """
        Initialize the population by creating p_size random harmonizations.
        """
        population = []
        
        for _ in range(self.p_size):
            c = Chromosome(self.line, self.line_voice)
            population.append(c)
        
        return population


    def evaluate(self):
        # Evaluate the fitness of each individual in the population
        for chrom in self.population:
            chrom._evaluate()
        


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
