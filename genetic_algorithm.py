from random import random
from individual import Individual
from population import Population


class GeneticAlgorithm:
    
    def __init__(self, population_size, mutation_rate, crossover_rate, elitism_count,dataset,capacity):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism_count = elitism_count
        self.dataset = dataset
        self.capacity = capacity
        
    def isUnique(self,individual1,individual2):
        for i in individual1.chromosome:
            for j in individual2.chromosome:
                if i.index == j.index:
                    return False
        return True
    
    def isContained(self,chromossome,individual):
        for i in individual.chromosome:
            if i.index == chromossome.index:
                True
        return False
    
    def init_population(self, chromosome_size):
        return Population(self.population_size, self.dataset ,chromosome_size)
        
    def calculate_fitness(self, individual):
        individual.fitness = 0
        individual.weight = 0
        for i in individual.chromosome:
            newFit = i.iloc[:,2:3].values[0][0]
            newWeight = i.iloc[:,1:2].values[0][0]
            if individual.weight + newWeight > self.capacity:
                individual.fitness = float('-inf')
                individual.weight = 0
                return float('-inf')
            else:
                individual.fitness += newFit
                individual.weight += newWeight
            
        return individual.fitness
        
        
    def evaluate_population(self, population):
        population_fitness = 0
        for i in range(population.size):
            population_fitness += self.calculate_fitness(population.individuals[i])
            
        population.fitness = population_fitness
        

    def select_parent(self, population):
        roulette_whell_position = random() * population.fitness
        spin_whell = 0
        for i in range(population.size):
            spin_whell += population.get_fittest(i).fitness
            if spin_whell >= roulette_whell_position:
                return population.get_fittest(i)
            
        return population.get_fittest(-1)
        
        
    def crossover_population(self, population):
        new_population = Population(population.size, population.dataset ,population.chromosome_size)
        
        cut_index = int(random() * population.chromosome_size)
        
        for i in range(population.size):
            parent1 = population.get_fittest(i)
            parent2 = Individual(population.chromosome_size,population.dataset)
            
            offspring = parent1
            
            if i > self.elitism_count and self.crossover_rate > random() and i >= cut_index:
                for j in range(parent2.chromosome_size):
                    adiconado = False
                    while not adiconado:
                        if not self.isContained(parent2.chromosome[j],offspring):
                            offspring.chromosome[j] = parent2.chromosome[j]
                            adiconado = True
                        else:
                            parent2 = Individual(population.chromosome_size,population.dataset)
                    
                    
            new_population.individuals[i] = offspring
            
        return new_population
    
    
    def mutate_population(self, population):
        new_population = Population(population.size,population.dataset ,population.chromosome_size)
        
        for i in range(population.size):
            individual = population.individuals[i]
            
            if self.mutation_rate > random():
                
                adiconado = False
                while not adiconado:
                    sam = Individual(population.chromosome_size,population.dataset)
                    if self.isUnique(sam,individual):
                        individual = sam
                        adiconado = True
                        break                    
                        
            new_population.individuals[i] = individual
        
        return new_population
    