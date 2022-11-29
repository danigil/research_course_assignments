import copy
import sys
from doctest import testmod
from itertools import permutations
from typing import List, Callable, Tuple
from abc import ABC



class OutputType(ABC):
    @classmethod
    def output(cls, tup: Tuple):
        """
        Return the required output based on the class type
        """
        raise NotImplementedError("Choose a specific output type")


class OutputPath(OutputType):
    @classmethod
    def output(cls, path: Tuple):
        return path


class OutputPathLength(OutputType):
    @classmethod
    def output(cls, path: Tuple):
        return len(path)


def check_2d_array_structure(l):
    """
    check_2d_array_structure
    assure that l is a nxn array filled with only ints

    >>> check_2d_array_structure([[1,2,3], [4,5,6], [7,8,9]])
    True
    >>> check_2d_array_structure('this should return false')
    False
    >>> check_2d_array_structure([])
    False
    >>> check_2d_array_structure([[], 'this should return false', []])
    False
    >>> check_2d_array_structure([[1],[2],[]])
    False
    >>> check_2d_array_structure([[1],[2],['this should return false']])
    False

    """
    if isinstance(l, list) and len(l) > 0 and \
            all([isinstance(item, list) for item in l]):
        n = len(l[0])
        return all([len(item) == n for item in l]) and all([isinstance(num, int) for item in l for num in item])
    else:
        return False


def TSP(algorithm: Callable, input_items, outputtype, **kwargs):
    """
    TSP
    input variant 1: Adjacency matrix - calculates TSP and outputs
    path or path length, output kwargs just for demonstration

    input variant 2: Adjacency matrix and set contatining indexes for cities - calculates TSP and outputs
    path or path length, output kwargs just for demonstration

    outputtype arg expecting OutputPath or OutputPathLength as input.



    >>> arr = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

    >>> TSP(brute_force_tsp,arr,outputtype=OutputPathLength)
    3
    >>> TSP(brute_force_tsp,arr,outputtype=OutputPath)
    (0, 1, 2)

    >>> TSP(brute_force_tsp,(arr,{0,1}),outputtype=OutputPathLength)
    2
    >>> TSP(brute_force_tsp,(arr,{0,1}),outputtype=OutputPath)
    (0, 1)

    >>> arr = [[0, 1, 10], [1, 0, 1], [10, 1, 0]]
    >>> TSP(brute_force_tsp,arr,outputtype=OutputPathLength,arg1='hello',arg2='flag')
    kwarg number 0: ('arg1', 'hello')
    kwarg number 1: ('arg2', 'flag')
    3

    >>> arr = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]
    >>> TSP(brute_force_tsp,(arr,{0,2}),outputtype=OutputPathLength)
    2
    >>> TSP(brute_force_tsp,(arr,{0,1,2}),outputtype=OutputPath)
    (0,2)

    """
    if isinstance(input_items, tuple):
        distance_matrix = input_items[0]
        cities_set = input_items[1]
    else:
        distance_matrix = input_items
        cities_set = range(len(input_items))

    return outputtype.output(algorithm(distance_matrix, cities_set, **kwargs))


def brute_force_tsp(distance_matrix, cities_set, **kwargs):
    [print(f'kwarg number {index}: {arg}') for index, arg in enumerate(kwargs.items())]

    min_tour_cost = sys.maxsize
    min_tour = tuple(cities_set)

    for perm in permutations(cities_set):
        current_tour_cost = 0
        for i in range(len(cities_set) - 1):
            current_tour_cost += distance_matrix[perm[i]][perm[i + 1]]
        if current_tour_cost < min_tour_cost:
            min_tour_cost = current_tour_cost
            min_tour = perm
    return min_tour


def shortest_route_tsp(distance_matrix, cities_set, **kwargs):
    def floyd_warshall(distance_matrix):
        if check_2d_array_structure(distance_matrix):
            n = len(distance_matrix)
            floyd = copy.deepcopy(distance_matrix)
            for i in range(n):
                floyd[i][i] = 0

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if floyd[i][j] > floyd[i][k] + floyd[k][j]:
                            floyd[i][j] = floyd[i][k] + floyd[k][j]

            return floyd
        else:
            return None

    [print(f'kwarg number {index}: {arg}') for index, arg in enumerate(kwargs.values())]
    floyd = floyd_warshall(distance_matrix)

    current_tour_cost = 0
    for i in range(len(cities_set) - 1):
        current_tour_cost += floyd[cities_set[i]][cities_set[i + 1]]

    return tuple(cities_set)


if __name__ == '__main__':
    testmod(name='assignment3_ex2', verbose=True)
