# Write a program to implement Genetic Algorithm

import os
import random

os.system("cls")

# Convert binary chromosome to decimal
def binary_to_decimal(chromosome):
    return int("".join(map(str, chromosome)), 2)


# Fitness function
def fitness(chromosome):
    x = binary_to_decimal(chromosome)
    return x * x


# Input chromosome length
length = int(input("Enter chromosome length: "))

# Input population size
population_size = int(input("Enter population size: "))

# Input number of generations
generations = int(input("Enter number of generations: "))

# Input mutation rate
mutation_rate = float(input("Enter mutation rate: "))


# Generate initial population
population = []

for i in range(population_size):
    chromosome = [
        random.randint(0, 1)
        for _ in range(length)
    ]
    population.append(chromosome)


# Genetic Algorithm
for generation in range(generations):

    # Calculate fitness
    fitness_values = [
        fitness(chromosome)
        for chromosome in population
    ]

    # Find best chromosome
    best_index = fitness_values.index(max(fitness_values))
    best_chromosome = population[best_index]
    best_fitness = fitness_values[best_index]

    print(
        f"Generation {generation + 1}: "
        f"{best_chromosome}  "
        f"x = {binary_to_decimal(best_chromosome)}  "
        f"Fitness = {best_fitness}"
    )

    # Selection
    selected = []

    for i in range(population_size):
        parent1 = random.choice(population)
        parent2 = random.choice(population)

        if fitness(parent1) > fitness(parent2):
            selected.append(parent1.copy())
        else:
            selected.append(parent2.copy())

    # Crossover
    new_population = []

    for i in range(0, population_size, 2):

        parent1 = selected[i]
        parent2 = selected[(i + 1) % population_size]

        # Select crossover point
        point = random.randint(1, length - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        new_population.append(child1)
        new_population.append(child2)

    # Mutation
    for chromosome in new_population:

        for i in range(length):

            if random.random() < mutation_rate:
                chromosome[i] = 1 - chromosome[i]

    # Create next generation
    population = new_population[:population_size]


# Final result
fitness_values = [fitness(chromosome) for chromosome in population]

best_index = fitness_values.index(max(fitness_values))
best_chromosome = population[best_index]

print("\nFinal Result:")
print("Best chromosome:", best_chromosome)
print("Best value of x:", binary_to_decimal(best_chromosome))
print("Maximum fitness:", fitness(best_chromosome))