from genetic_algorithm import GeneticAlgorithm
import pandas as pd
import copy

#from IPython.display import display

dataset = pd.read_csv('data/database.csv', delimiter=';')
x = dataset.iloc[ : ,0:3]
capacidade = int(dataset.iloc[:,3:4].values[0][0])

generation = 0
ga = GeneticAlgorithm(15, 0.10, 0.97, 3,x, capacidade)

population = ga.init_population(8)
population.generation = generation
ga.evaluate_population(population)
fittest_indv = copy.deepcopy(population.get_fittest())


while generation < 200:
    
    #print(f'Best solution: {fittest_indv.fitness} / {fittest_indv.weight}')
    #print(f'Geracao: {generation}')
    
    generation += 1
    population = ga.crossover_population(population)
    population = ga.mutate_population(population)
    ga.evaluate_population(population)
    population.generation = generation
    
    evalpop = population.get_fittest()
    
    if evalpop.fitness > fittest_indv.fitness:
        print (f' New Best Value: {evalpop.fitness} found at Generation {generation}')
        fittest_indv = copy.deepcopy(evalpop) 
    
    
print()
print()
print(f'Found solution in {generation} generations')
print()
print(f'Best Fitness: {fittest_indv.fitness} - weight: {fittest_indv.weight}') 
print()
print('Mochila:')
mochila = [0 for i in range(len(x.index)-1)]
for i in fittest_indv.chromosome:
    mochila[i.index[0]] = 1
print(mochila)
print()
print('Objects:')