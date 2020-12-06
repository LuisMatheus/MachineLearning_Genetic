from individual import Individual

class Population:
    
    def __init__(self, population_size, dataset ,chromosome_size=10):
        self.size = population_size
        self.chromosome_size = chromosome_size
        self.fitness = 0
        self.generation = 0
        self.dataset = dataset
        self.individuals = [ Individual(chromosome_size,dataset) for i in range(population_size) ]
        
    def get_fittest(self, offset=0):
        return sorted(self.individuals, key=lambda individual: individual.fitness, reverse=True)[offset]