from doctest import testmod
from queue import Queue
from typing import Tuple


def f1(x: int, y: int, z):
    return x + y + z


def safe_call(func, *args):
    """safe_call receives function, args for that function and calls the function
     with those args if they match the annotations, otherwise throws exception.

    #Examples where the function will work correctly:
    >>> safe_call(f1,5,5,5)
    15

    >>> safe_call(f1,5,5,5.7)
    15.7

    #Example where the function should throw an exception:
    >>> safe_call(f1,5.0,"hello",'z')
    Traceback (most recent call last):
     ...
    Exception
     """

    for arg, annot in zip(func.__annotations__.values(), (type(val) for val in args)):
        if arg is not annot:
            raise Exception

    print(func(*args))


def four_neighbor_function(node):
    x, y = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def breadth_first_search(start: Tuple[int, ...], end: Tuple[int, ...], func):
    predecessors = {}

    Q = Queue()
    Q.put(start)

    visits = set()
    visits.add(start)

    while not Q.empty():
        current = Q.get()
        if current == end:
            break
        for neighbour in func(current):
            if neighbour not in visits:
                Q.put(neighbour)
                predecessors[neighbour] = current

        visits.add(current)

    def print_path(start, end):
        if start == end:
            print(start)
        elif end not in predecessors:
            print("no path")
        else:
            print_path(start, predecessors[end])
            print(end)

    print_path(start, end)


if __name__ == '__main__':
    # testmod(name='safe_call', verbose=True)
    breadth_first_search((0, 0), (1, 3), four_neighbor_function)
