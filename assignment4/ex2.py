from doctest import testmod

import numpy
from networkx.generators.random_graphs import fast_gnp_random_graph, gnp_random_graph
from networkx.algorithms.approximation.clique import max_clique as approx_max_clique
from networkx.algorithms.clique import graph_clique_number as opt_max_clique_size

import matplotlib.pyplot as plt


def approximation_ratio(n):
    """
    approximate solution is guarenteed to be OPT*O(n/logn^2) where n is the amount of nodes in the graph

    Boppana, R., & Halldórsson, M. M. (1992).
    Approximating maximum independent sets by excluding subgraphs. BIT Numerical Mathematics, 32(2), 180–196. Springer. doi:10.1007/BF01994876

    >>> [(i,round(approximation_ratio(i))) for i in range(10, 120, 10)]
    [(10, 1), (20, 1), (30, 1), (40, 1), (50, 2), (60, 2), (70, 2), (80, 2), (90, 2), (100, 2), (110, 2)]

    approximation_ratio(10) = 1 (rounded)
    approximation_ratio(50) = 2 (rounded)
    approximation_ratio(200) = 3 (rounded)
    """
    return numpy.divide(n, numpy.power(numpy.log2(n), 2))


def return_approx_opt_solutions(n, p):
    """
    returns approximate solution and optimal solution.

    >>> return_approx_opt_solutions(2,1)
    (2, 2)

    >>> return_approx_opt_solutions(6,1)
    (6, 6)

    >>> return_approx_opt_solutions(50,1)
    (50, 50)
    """
    if p > 0.5:
        G = gnp_random_graph(n, p)
    else:
        G = fast_gnp_random_graph(n, p)

    approx = len(approx_max_clique(G))
    opt = opt_max_clique_size(G)

    return approx, opt


lower_bound = 10 # lower bound for number of nodes - change to control the system
upper_bound = 50 # upper bound for number of nodes - change to control the system

node_sizes = range(lower_bound, upper_bound)
probabilities = [0.2, 0.4, 0.6, 0.8, 0.9, 1] # I chose to calculate 5 non-trivial probabilites and the trivial one as well.


def plot(actual_ratios, index): # plot one of the sublots.
    plt.subplot(2, 3, index + 1)

    plt.plot(node_sizes, actual_ratios, label='Actual Ratios')
    plt.plot(node_sizes, [1 / approximation_ratio(n) for n in node_sizes], label='Bound Ratios')

    plt.xlabel("Value of n")
    plt.ylabel("Approx ratio")
    plt.title(f'p={probabilities[index]}')


if __name__ == '__main__':
    testmod(name='assignment4_ex2', verbose=True)

    for index, p in enumerate(probabilities):
        actual_ratios = []
        for n in node_sizes:
            calc = return_approx_opt_solutions(n, p)

            actual_ratios.append(numpy.divide(calc[0], calc[1]))
            print(
                f"n={n}, p={p}, approx={calc[0]}, opt={calc[1]}, guaranteed_mathematically (this is big O so it can "
                f"be a little off)={numpy.round(calc[1] * (1 / approximation_ratio(n)))}")
        plot(actual_ratios, index)

    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
