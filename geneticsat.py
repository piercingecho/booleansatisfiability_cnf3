import random
from Solution import *
from cnfinstance import *
from sat_util import *


random.seed(42)

def createStartingBunch(population, literals, rules):
    num_literals = len(literals)
    pop = []
    for i in range(population):
        curr = []
        for j in range(num_literals):
            curr.append(random.randint(0,1))
        pop.append(Solution(curr, numSatisfied(literals, curr, rules)))

    return pop

def propagate(population, literals, rules):
    # top half of population propagates. Two parents make two children, so
    # we double the population beforehand to keep the population size constant.

    childmakers = population[:len(population) // 2] # i hate arrays that make children
    childmakers = childmakers * 2
    random.shuffle(childmakers)
    new_pop = []
    while(childmakers):
        maker_one = childmakers.pop(0).literal_values
        maker_two = childmakers.pop(0).literal_values
        child_one, child_two = make_children(maker_one, maker_two, literals, rules)
        new_pop.append(child_one)
        new_pop.append(child_two)
    return new_pop

def make_children(maker_one, maker_two, literals, rules):
    #input two arrays, gives back two Solution objects.
    segment_length = len(maker_one) // 8
    child_one = maker_one.copy()
    child_two = maker_two.copy()
    for i in range(segment_length):
        #current index should loop back around to the start, hence % len(maker_one) 
        index = i + segment_length % len(maker_one)
        child_one[index], child_two[index] = child_two[index], child_one[index]

    solution_one = Solution(child_one, numSatisfied(literals, child_one, rules))
    solution_two = Solution(child_one, numSatisfied(literals, child_one, rules))
    return solution_one, solution_two

def mutate(solution, literals, rules):
    curr = solution.literal_values
    chosen_index = random.randint(0, len(curr) - 1)
    if(curr[chosen_index] == 1):
        curr[chosen_index] = 0
    else:
        curr[chosen_index] = 1

    newSolution = Solution(curr, numSatisfied(literals, curr, rules))
    return newSolution

def geneticSAT(literals, rules):
    # Takes in a boolean satisfiability object, and
    # returns a list of variables that maximize the
    # number of variables set to "True".
    # Does so in a brute-force fashion. 
    
    POP_SIZE = 100 # MUST be a multiple of 4 to maintain size of population.
    NUM_ITER = 75
    MUTATION_RATE = 0.0001
    
    num_literals = len(literals)
    num_rules = len(rules)

    population = createStartingBunch(POP_SIZE, literals, rules)

    best_solns = [0] * NUM_ITER
    curr_best_soln = None

    for i in range(NUM_ITER):

        population.sort(reverse = True)
        if(curr_best_soln == None or population[0] > curr_best_soln):
            curr_best_soln = population[0]
        best_solns[i] = curr_best_soln

        #now update children and mutate

        population = propagate(population, literals, rules)

        #mutate
        for i in range(len(population)):
            if(random.uniform(0.0, 1.0) < MUTATION_RATE):
                population[i] = mutate(population[i], literals, rules)

    return best_solns




def main():
    literals, rules = makeCNFInstance("biginput.txt")
    #a = createStartingBunch(50, literals, rules)
    #print(a)
    
    a = geneticSAT(literals, rules)
    print(a)
    #literals, rules = makeCNFInstance("biginput.txt")
    #best_soln = bruteForceSAT(literals, rules)

    #print(best_soln)


if __name__ == '__main__':
    main()