from utility.find_key import KeyEstimator
from utility.get_voice import get_voice

class EvoComposer:
    def __init__(self, melody_stream, generations=100, population_size=100, crossover_rate=0.7, mutation_rate=0.01):
        self.input_melody_stream = melody_stream
        key_estimator = KeyEstimator()
        self.input_melody_key = key_estimator(melody_stream)
        self.input_melody_voice = get_voice(melody_stream)
        
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.population = []


    def initialize_population(self):
        # Initialize the population with random individuals
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