"""
Write a function roulette_wheel_select(population, fitness, r) that takes a list of individuals, a fitness function, and a floating-point random number r in the interval [0, 1), and selects and returns an individual from the population using the roulette wheel selection mechanism. The fitness function (which will be provided as an argument) takes an individual and returns a non-negative number as its fitness. The higher the fitness the better. When constructing the roulette wheel, do not change the order of individuals in the population.
"""
import random
def roulette_wheel_select(population, fitness, r):
    t = sum(fitness(i) for i in population)
    N = r * t
    total = 0
    for i in range(t):
        total += fitness(population[i])
        if N <= total:
            return population[i]
    return population[-1]

def main():
    print('test 1')
    population = ['a', 'b']
    
    def fitness(x):
        return 1 # everyone has the same fitness
    
    for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
        print(roulette_wheel_select(population, fitness, r))    
    
    print()
    print('test 2')
    population = [0, 1, 2]
    
    def fitness(x):
        return x
    
    for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
        print(roulette_wheel_select(population, fitness, r)) 
        
    print()
    print('test 3')
    population = ['a', 'b', 'c', 'd', 'e']
    
    def fitness(x):
        return [0, 0, 1, 0, 2][ord(x) - ord('a')]
    
    for r in range(1, 23):
        print(roulette_wheel_select(population, fitness, r/23))    
    
if __name__ == '__main__':
    main()