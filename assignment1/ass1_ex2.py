from doctest import testmod
from queue import Queue


def four_neighbor_function(node):
    x, y = node
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def breadth_first_search(start, end, func):
    """
    breadth_first_search
    receives start node, end node, function that returns neighbours of a node
    performs BFS search when a path from start to end is found, it is printed and the function ends.

    the function is implemented with the assumption that == operator,__repr__ exists for start and end objects

    ##Good Cases (Shouldn't throw)
        >>> breadth_first_search((0,0),(1,3),four_neighbor_function)
        (0, 0) -> (0, 1) -> (0, 2) -> (0, 3) -> (1, 3)

    """
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
            print(start, end="")
        elif end not in predecessors:
            print("no path")
        else:
            print_path(start, predecessors[end])
            print(" ->", end, end="")

    print_path(start, end)

if __name__ == '__main__':
    testmod(name='assignment1_ex2', verbose=True)