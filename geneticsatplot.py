import random
from Solution import *
from cnfinstance import *
from sat_util import *
from geneticsat import *
import numpy as np
import matplotlib.pyplot as plt

def plot_output(best_solns, num_clauses):

    x_data = np.array(list(i for i in range(len(best_solns))))
    y_data = list(soln.clauses_fulfilled for soln in best_solns)

    plt.plot(x_data, y_data, linestyle='-', marker='o')
    plt.xlabel('Generation number')
    ylabel = 'Number of Clauses Fulfilled (out of ' + str(num_clauses) + ')'
    plt.ylabel(ylabel)
    plt.title('Solution Quality over Time')
    plt.ylim(0, num_clauses * 1.25)
    fig = plt.gcf() # In order to save, this line MUST be in the same cell as plt.plot()!
    fig.savefig("figureTwo.png")

def main():
    
    literals, rules = makeCNFInstance("biginput.txt")
    #a = createStartingBunch(50, literals, rules)
    #print(a)
    
    genetic_solns = geneticSAT(literals, rules)
    plot_output(genetic_solns, len(rules))
    
    #literals, rules = makeCNFInstance("biginput.txt")
    #best_soln = bruteForceSAT(literals, rules)

    #print(best_soln)

if __name__ == '__main__':
    main()