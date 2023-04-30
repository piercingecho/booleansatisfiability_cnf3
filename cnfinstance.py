def makeCNFInstance(inputfile = "input.txt"):
    # ex: 1,2,3|-4,5,-6

    variables = []
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
            bool_value = (var > 0)
            var_value = abs(var)

            if(not(var_value in variables)):
                variables.append(var_value)

            new_rule.append((var_value, bool_value))

        rules.append(new_rule)

    return variables, rules


def main():
    variables, rules = makeCNFInstance()
    print(variables)
    for rule in rules:
        print(rule)

if __name__ == '__main__':
    main()