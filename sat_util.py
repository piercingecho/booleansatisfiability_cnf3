def numSatisfied(literals, literal_values, rules):
    #takes in a set of literals, literal values, and rules, and returns the number of clauses that are satisfied.
    num_satisfied = 0
    for rule in rules:
        if(ruleSatisfied(literals, rule, literal_values)):
            num_satisfied += 1
    
    return num_satisfied

def ruleSatisfied(literals, rule, literal_values):
    for literal in rule:
        location = literals.index(abs(literal))
        # if true with negative value, or false with positive value, it's not valid.
        if((literal_values[location] and literal > 0) or 
           (not literal_values[location] and literal < 0)):
           return True

    return False