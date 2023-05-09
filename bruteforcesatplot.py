import random
from bruteforcesat import *
from backtrackingsat import *
from Solution import *
from cnfinstance import *
from sat_util import *
from geneticsat import *
from createthreesat import *
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

def plot_output(x_data, y_data):

    plt.plot(x_data, y_data, linestyle='-', marker='o')
    plt.xlabel('Number of Literals number ($N$)')
    ylabel = 'Time to Search Entire Space (in seconds)'
    plt.ylabel(ylabel)
    plt.title('Time to Completely Search State Tree')
    plt.legend(["Brute Force", "Brute Force with Backtracking"])
    fig = plt.gcf() 
    fig.savefig("figureOne.png")

def main():
    #    x_data = [7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    x_data = [6,7,8,9,10,11,12,13,14,15,16,17]
    y_data = []
    num_iter_to_average = 5
    filename = "plottedinput.txt"
    for num_literals in x_data:
        y_avgs = []
        bruteforcelist = []
        backtrackinglist = []

        for i in range(5):
            createThreeSatFile(num_literals, 500, filename)
            literals, rules = makeCNFInstance(filename)
            start_time = time.time()
        
            #brute force
            best_soln = bruteForceSAT(literals, rules)
            end_time = time.time()
            
            bruteforcelist.append(end_time - start_time)

            start_time = time.time()

            #backtracking
            best_soln = backtrackingSAT(literals, rules)

            end_time = time.time()
            backtrackinglist.append(end_time - start_time)


        y_avgs.append(sum(bruteforcelist) / num_iter_to_average)
        y_avgs.append(sum(backtrackinglist) / num_iter_to_average)
        y_data.append(y_avgs)

    plot_output(x_data, y_data)

if __name__ == '__main__':
    main()