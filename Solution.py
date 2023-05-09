# curr_solution = Solution(combination, numSatisfied(literals, combination, rules))

class Solution:
    def __init__(self, literal_values, clauses_fulfilled):
        self.literal_values = literal_values
        self.clauses_fulfilled = clauses_fulfilled
        self.numTrue = literal_values.count(1)


    def __lt__(self, that):
        if(self.clauses_fulfilled != that.clauses_fulfilled):
            return self.clauses_fulfilled < that.clauses_fulfilled

        return self.numTrue < that.numTrue
        

        return self.literal_values

    def addLiterals(self, literals):
        self.literals = literals

    def __str__(self):
        s = ""
        for i, lit in enumerate(self.literals):
            if(not self.literal_values[i]):
                s += "-"
            s += str(lit)
            s += " "
    
        return s