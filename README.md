# booleansatisfiability_cnf3

The implementation here was in order to write an analysis comparing designs of ways to approach an NP-Complete problem. The document's content is appended below. 

To reconstruct Figure One, please run bruteforcesatplot.py in a terminal window.

To reconstruct Figure Two, please run geneticsatplot.py in a terminal window.

Sample input files are attached for utilizing bruteforcesat.py, backtrackingsat.py, and geneticsat.py. In their main() definitions, you can alter which file is used. The main() file should be the main reference as a guide to using parts of this implementation in other programs. To create an procedurally generated instance of three-CNF for testing, alter the variables at the beginning of createthreesat.py.

### 3-CNF Boolean Satisfiability: Optimizations and Considerations

The problem specifies a logical expression as an input, composed of a set of literals (True/False values) N. They are combined with ‘not’, ‘and’, and ‘or’, and are tasked with finding an assignment that satisfies the logical expression. If there are multiple satisfying assignments, we must maximize the number of literals set to True. We are given a problem with n literals.

The expression is in 3-CNF form (3 Conjunctive Normal Form), where there are a selection of up to three literals “or”ed together (unioned), that are all “and”ed together (intersected). Let each unioned set be called a ‘clause,’ and c be the number of clauses. In input files, we assume exactly three literals per clause, as dummy variables could be created for the case of less than three literals unioned. We assume the literals are corresponding to integers, negative integers implying “not”. Unions are denoted by commas, and intersections are denoted by bars. An example input string would be as follows: “14,20,10|-7,6,-19|-11,16,-9”.

#### Brute Force and The Search Space

A candidate solution is an assignment of these literals to ‘True’ or ‘False’. To test a candidate solution, we must go through every clause and validate that these assignments are valid. This time increases linearly based on the number of clauses.
All possible candidates are all possible assignments of literals. Because literals are independently assigned, the Fundamental Counting Principle suggests that the search space is 2n. So to check the entire search space by brute force, this will be ϴ(c*2n). Because the number of clauses only linearly affects the theoretical runtime of 3-CNF and the length of clauses is constant, we keep the number of clauses constant in figures and discussion.

To do this problem by brute force leaves much to be desired, as we can recognize that an assignment is not promising early. For instance, if there exists the clause “-1,-2,-3”, and all three of those literals are True, then all derived solutions will not fulfill the logistic expression. The pruning of a single such contradiction removes ⅛ of the search space. Our backtracking algorithm exploits this. We begin by sorting the literals by their frequency in each clause, so that we traverse the most commonly used ones first. This allows us to backtrack earlier, as we reach more clauses to validate faster. The results are in Figure 1, where this method of backtracking shows a shocking improvement in the runtime of the program.

#### Heuristics for Maximizing Number of True Literals

The following is written under the assumption that there exist a set of solutions S that satisfy the logical expression, and that we now wish to only explore the paths that can have more literals set to True than our current best solution. We can further elaborate on our backtracking technique, in order to add pruning. The maximum number of “True” literals of a derived solution is n minus the number of literals set to False. If this number is less than the amount of literals assigned to True in our current best solution, then no derived solution will be able to be better than our best known solution. So, we can prune all derived solutions.

#### Heuristics for Maximizing Number of True Clauses

Finding a satisfying assignment of literals is NP-Complete, so without trying every solution there is potential for a completely satisfiable one to be missed through an implementation such as a greedy approach. But even for SAT problem instances where there is nothing completely satisfiable, there may be a desire to maximize the number of clauses that equate to True. An immediately apparent way to maximize the number of clauses may be to sort the literals by frequency of them being assigned True, and then prioritizing the search space of those near the end of the sorted collection. This means that the most frequently occurring literals will be set to True, hence creating an immediately large number of clauses that equate to True. The search space of the end will be slight optimizations of the initial boost to the number of True clauses we achieve from setting literals near the beginning to True.
From these somewhat greedy solutions, we wish to devise a genetic algorithm that will search more of the relevant space, and potentially do better than these initial guesses. Because our set of literals to consider are only True/False, we can represent our assignments as a binary string. A child from two parents may be represented as each bit being randomly chosen from either the first or second parent’s value, and a mutation is a random bit being swapped. This will quickly go through the search spaces that may be relevant in a relatively short amount of time. Of course, genetic algorithms have no guarantees, but because they generally require few iterations to get decent results (and they approach local optima rather quickly), we can gain good results from them here. Figure 2 highlights our implementation of a genetic algorithm, which shows that it almost instantly reaches a local maximum after the greedy approach. The nature of SAT problems having unpredictable satisfying assignments implies that similar places in the search space will have varied results, and so the flaw of genetic algorithms in reaching a local maximum is exacerbated.


#### Description of Figures
Figure 1. This was taken as an average of 5 random generations of a SAT problem with the given number of literals and 520 clauses. Brute force is not calculated above n=17 because the exponential trend continues. Note that backtracking’s effectiveness depends on the exact instance of the problem we have, and so its increase is less predictable.

Figure 2. A genetic algorithm variant of size 50 was used, with 75 iterations. This is on a test of 500 variables and 10,000 random clauses to satisfy. This is a circumstance where, given the luck of how the file was generated, there is likely no way to truly satisfy the expression. As seen, the algorithm fairly quickly reaches a local maximum, but it is a high proportion of the clauses fulfilled.
