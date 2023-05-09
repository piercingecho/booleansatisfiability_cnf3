from Solution import *
from cnfinstance import *
from sat_util import *

def decrement(bitlist):
    i = len(bitlist) - 1
    while(bitlist[i] == 0 and i >= 0):
        bitlist[i] = 1
        i -= 1
    if(i != -1):
        bitlist[i] = 0

def bruteForceSAT(literals, rules):
    # Takes in a boolean satisfiability object, and
    # returns a list of variables that maximize the
    # number of variables set to "True".
    # Does so in a brute-force fashion. 
    
    num_literals = len(literals)
    num_rules = len(rules)
    # we use a list of 'bits', 0 or 1, to depict true or false. This works because of python boolean rules.
    original_combination = [0 for i in range(num_literals)]
    best_solution = Solution(original_combination, numSatisfied(literals, original_combination, rules))

    combination = original_combination.copy()
    decrement(combination)

    while(combination != original_combination):
        curr_solution = Solution(combination, numSatisfied(literals, combination, rules))

        if(curr_solution > best_solution):
            best_solution = curr_solution

        ###
        ### Here, we have the current best solution. If desired, we can store the viability of it in an array
        ### for figures. 
        ###

        combination = combination.copy()
        decrement(combination)

    best_solution.addLiterals(literals) # for string formatting later.
    return best_solution


def main():
    literals, rules = makeCNFInstance("biginput.txt")
    best_soln = bruteForceSAT(literals, rules)

    print(best_soln.clauses_fulfilled)


if __name__ == '__main__':
    main()