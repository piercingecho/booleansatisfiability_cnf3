def makeCNFInstance(inputfile = "input.txt"):
    # ex: 1,2,3|-4,5,-6

    literals = []
    # [1,2,3,4,5,6]
    rules = []
    # [[(1, True), (2, True), (3, True)],
    # [(4, False), (5, True), (6, False)]]
    
    with open(inputfile) as f:
        s = f.readline()

    clauses = s.split("|")
    for clause in clauses:
        clause_vars = clause.split(",")
        new_rule = []
        for strf_var in clause_vars:
            var = int(strf_var)
            var_value = abs(var)

            if(not(var_value in literals)):
                literals.append(var_value)

            new_rule.append(var)

        rules.append(new_rule)

    return literals, rules


def main():
    literals, rules = makeCNFInstance()
    print(literals)
    for rule in rules:
        print(rule)

if __name__ == '__main__':
    main()