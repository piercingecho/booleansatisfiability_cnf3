from Solution import *
from cnfinstance import *
from sat_util import *

def backtrackingSAT(literals, rules):
    # sort the literals based on frequency of literal in ruleset.
    lits = sorted(literals, key = lambda x: rules.count(x), reverse = True)

    soln_a = backtrackRecursive(lits, rules, [0])
    soln_b = backtrackRecursive(lits, rules, [1])

    best_soln = max(soln_a, soln_b)

    return best_soln

def promising(literals, rules, literal_values):
    for rule in rules:
        isContradicting = True
        # return false if one rule is contradicted.
        for literal in rule:
            location = literals.index(abs(literal))
            if(location >= len(literal_values)):
                isContradicting = False
                break
            # if true with negative value, or false with positive value, it's not valid.
            if((literal_values[location] and literal > 0) or 
                (not literal_values[location] and literal < 0)):
                isContradicting = False
                break

        if(isContradicting):
            return False

    return True

def backtrackRecursive(literals, rules, literal_values):
    if(promising(literals, rules, literal_values)):
        if(len(literal_values) < len(literals)):
            #partial solution.
            new_list_a = literal_values.copy()
            new_list_a.append(0)
            soln_a = backtrackRecursive(literals, rules, new_list_a)
            new_list_b = literal_values.copy()
            new_list_b.append(1)
            soln_b = backtrackRecursive(literals, rules, new_list_b)
            return max(soln_a, soln_b)
        else:
            return Solution(literal_values, numSatisfied(literals, literal_values, rules))

    else:
        # dummy solution returned, this is a bad part.
        return Solution([0], 0)


def main():
    literals, rules = makeCNFInstance("biginput.txt")
    best_soln = backtrackingSAT(literals, rules)
    best_soln.addLiterals(literals)
    print(best_soln)


if __name__ == '__main__':
    main()