import random

def createThreeSatFile(maxNumVar, numClause, outfile):

    s = ""
    nums = list(i for i in range(1, maxNumVar))
    for j in range(numClause):
        for i in range(3):
            # half chance for it to be "Not"
            if(random.randint(0,1)):
                s += "-"
            
            if(nums):
                index = random.randint(0, len(nums) - 1)
                s += str(nums[index])
                nums.pop(index)
            else:
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

    return len(clauses), len(variables)


def main():
    outfile = 'beeginput.txt'
    createThreeSatFile(35, 500, outfile)

    numclause, numvar = countThreeSatFile(outfile)
    print("number variables:", numvar)
    print("number clauses:", numclause)
if __name__ == '__main__':
    main()