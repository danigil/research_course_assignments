import networkx as nx
import numpy
from networkx.generators.random_graphs import fast_gnp_random_graph, gnp_random_graph
from networkx.algorithms.approximation.clique import max_clique as approx_max_clique
from networkx.algorithms.clique import graph_clique_number as opt_max_clique_size

import matplotlib.pyplot as plt


def approximation_ratio(n):
    return numpy.divide(n, numpy.power(numpy.log2(n), 2))


def compare(n, p):
    if p > 0.5:
        G = gnp_random_graph(n, p)
    else:
        G = fast_gnp_random_graph(n, p)

    approx = len(approx_max_clique(G))
    opt = opt_max_clique_size(G)

    return approx, opt


node_sizes = range(10, 90)
probabilities = [0.2, 0.4, 0.6, 0.8, 0.9, 1]


def plot(actual_ratios, index):
    plt.subplot(2, 3, index + 1)
    plt.plot(node_sizes, actual_ratios, label='Actual Ratios')
    plt.plot(node_sizes, [1 / approximation_ratio(n) for n in node_sizes], label='Bound Ratios')
    plt.xlabel("Value of n")
    plt.ylabel("Approx ratio")
    plt.title(f'p={probabilities[index]}')


if __name__ == '__main__':
    # node_sizes = [10 ** i for i in range(1, 4)]

    for index, p in enumerate(probabilities):
        actual_ratios = []
        for n in node_sizes:
            calc = compare(n, p)

            actual_ratios.append(numpy.divide(calc[0], calc[1]))
            print(f"n={n}, p={p}, approx={calc[0]}, opt={calc[1]}, guaranteed_mathematically={numpy.round(calc[1]*(1/approximation_ratio(n)))}")
        plot(actual_ratios, index)

    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
