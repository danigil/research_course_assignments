import time
from doctest import testmod

import cvxpy as cp
from cvxpy import SolverError
from cvxpy.atoms.affine.add_expr import AddExpression

import numpy as np

import matplotlib.pyplot as plt

"""
store different solvers here to use with cvxpy, unfortunately most of them refuse
to work for me for various reasons, on other systems that have the solvers installed correctly, 
these can be theoretically be added as well, the code is made with the intention of comparing them all for fun :)

solvers list:
OSQP, ECOS, GLOP, MOSEK, CBC, CVXOPT, NAG, PDLP, GUROBI, and SCS
"""
solvers = [cp.OSQP, cp.GUROBI, cp.SCS]


def generate_random_linear_equation_system(rank: int, rng=np.random.default_rng()):
    scalars = rng.integers(10, size=(rank, rank))
    solutions = rng.integers(100, size=rank)
    #
    # x_value = np.linalg.solve(scalars, solutions)
    #
    # # print(f'x1 = {x_value[0]}, x2 = {x_value[1]}')
    # print(x_value)
    #
    # variables = cp.Variable(rank)
    # constraints = [scalars @ variables == solutions]
    #
    # obj = cp.Minimize(AddExpression(variables))
    #
    # prob = cp.Problem(obj, constraints)
    # prob.solve()
    #
    # print(variables.value)

    return scalars, solutions


def np_solve(scalars, solutions):
    """
    np_solve

    solve a linear equation system using numpy linalg.solve
    >>> np.allclose(np_solve(np.array([[1,1],[1.5,4]]), np.array([2200,5050])), np.array([1500.0, 700.0]))
    True

    """

    return np.linalg.solve(scalars, solutions)


def cvxpy_solve(scalars, solutions, solver=cp.SCS):
    """
    cvxpy_solve

    solve a linear equation system using cvxpy solvers
    >>> np.allclose(cvxpy_solve(np.array([[1,1],[1.5,4]]), np.array([2200,5050])), np.array([1500.0, 700.0]))
    True


    """
    variables = cp.Variable(len(solutions))
    constraints = [scalars @ variables == solutions] # Ax = b constraints

    obj = cp.Minimize(AddExpression(variables))

    prob = cp.Problem(obj, constraints)
    prob.solve(solver=solver)

    return variables.value


def time_function(func, *args, **kwargs):
    """
    runs func and times it, returning a tuple like so: (func_output, time it took to calc)
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()

    total_time = end_time - start_time

    return result, total_time


def plot_runtime(lib_name, time_measurements):
    """
    plot_runtime takes one measurement set from one type of solution and plots it
    """
    plt.plot(range(1, len(time_measurements) + 1), time_measurements, label=lib_name)


if __name__ == '__main__':
    testmod(name='assignment4_ex1', verbose=True)

    MAX_RANK = 200
    """
    ^
    |
    Number that dictates what how many ranks to generate a randomized linear equation system for.
    On my computer it seems as though calculations with rank > 200 take too long.
    """

    times_numpy = []
    times_cvxpy = [[] for _ in solvers]
    for i in range(1, MAX_RANK + 1):
        tup = generate_random_linear_equation_system(i)

        times_numpy.append(time_function(np_solve, *tup)[1])

        for index, solver in enumerate(solvers):
            times_cvxpy[index].append([time_function(cvxpy_solve, *tup, solver)[1]])

    plot_runtime("NUMPY", times_numpy)

    for index, solver in enumerate(solvers):
        plot_runtime(f"CVXPY ({solver})", times_cvxpy[index])

    plt.xlabel("Rank")
    plt.ylabel("Seconds")
    plt.title("LINEAR EQUATION SYSTEM SOLVE TIME COMPARISON")
    plt.legend(loc='best')
    plt.show()
