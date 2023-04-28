import random

def createThreeSatFile(maxNumVar, numClause, outfile):
    # Note: no guarantee this will have exactly maxNumVar variables.
    # This is because it is generated randomly. So, a way to count the
    # number of variables and clauses is in countThreeSatFile.

    s = ""
    for j in range(numClause):
        for i in range(3):
            # half chance for it to be "Not"
            if(random.randint(0,1)):
                s += "-"
            
            s += str(random.randint(1, maxNumVar))

            # variable delimiter
            if(i != 2):
                s += ","
        # absolute value delimiter
        if(j != numClause - 1):
            s += "|"

    with open(outfile, "w") as f:
        f.write(s)

def countThreeSatFile(infile):
    with open(infile) as f:
        s = f.readline()
    clauses = s.split("|")
    variables = []
    for clause in clauses:
        curr = clause.split(",")
        # curr is a list of three variables, that could be negative.
        for var in curr:
            updated_var = abs(int(var))
            
            if not(updated_var in variables):
                variables.append(updated_var)

    print(variables)
    return len(clauses), len(variables)


def main():
    createThreeSatFile(10, 10, "biginput.txt")

    numclause, numvar = countThreeSatFile("biginput.txt")
    print("number variables:", numvar)
    print("number clauses:", numclause)
if __name__ == '__main__':
    main()