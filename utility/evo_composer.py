from music21 import *
from utility.chromosome import Chromosome

class EvoComposer:
    def __init__(self, melody, voice, population_size=5, prob_crossover=0.7, prob_mutation=0.01, generations_count=100):
        self.melody = melody
        self.voice = voice
        self.population_size = population_size
        self.prob_crossover = prob_crossover
        self.prob_mutation = prob_mutation
        self.generations_count = generations_count


    def initialize_population(self):
        """
        Initialize the population by creating p_size random harmonizations.
        """
        self.population = []
        for _ in range(self.population_size):
            c = Chromosome(self.melody, self.voice)
            c.harmonize()

            self.population.append(c)


    def evaluate(self):
        # Evaluate the fitness of each individual in the population
        for chrom in self.population:
            eval_harmonic, eval_melodic = chrom._evaluate()
            # print(eval_harmonic)
            # print(eval_melodic)


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
