from doctest import testmod
from queue import Queue


def f1(x: int, y: int, z):
    return x + y + z


def safe_call(func, *args):
    """
    safe_call
    receives function, args for that function and calls the function
    with those args if they match the annotations, otherwise throws exception.

    ##Good Cases (Shouldn't throw)
        >>> safe_call(f1,5,5,5)
        15

        >>> safe_call(f1,5,5,5.7)
        15.7

    ##Bad Cases (Should throw)
        #mismatching annotation
        >>> safe_call(f1,5.0,"hello",'z')
        Traceback (most recent call last):
         ...
        Exception

        #incorrect order
        >>> safe_call(f1,"1",1,1)
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


def print_sorted(obj):
    """
    print_sorted
    receives a variable (can be a data structure (nested or not) or a primitive var)
    and prints it sorted in all nested levels.

    >>> print_sorted({'a': 5, 'c': 6, 'b': [1, 3, 2]})
    {"a": 5, "b": [1, 2, 3], "c": 6}
    >>> print_sorted((7,5,[8,5,8,(2,1)]))
    ([(1, 2), 5, 8, 8], 5, 7)

    """

    # choose key is used to allow sorted() to be able to compare Data structures and other objects
    def choose_key(x):
        if type(x) in (list, dict, tuple, set):
            return len(x)
        else:
            return x

    def print_no_new_line(obj):
        print(obj, end="")

    """
        the following 4 methods are used to print each ds 
        according to its representation and then recurse on the inner objects
    """

    def print_sorted_list(l: list):
        flag = False
        print("[", end="")

        for item in sorted(l, key=choose_key):
            if flag:
                print(", ", end="")
            funcs_dict.get(type(item), print_no_new_line)(item)
            flag = True
        print("]", end="")

    def print_sorted_dict(d: dict):
        flag = False
        print("{", end="")
        for key in sorted(d):
            if flag:
                print(", ", end="")
            print(f"\"{key}\": ", end="")
            funcs_dict.get(type(d[key]), print_no_new_line)(d[key])
            flag = True
        print("}", end="")

    def print_sorted_set(s: set):
        flag = False
        print("{", end="")
        for item in s:
            if flag:
                print(", ", end="")
            funcs_dict.get(type(item), print_no_new_line)(item)
            flag = True
        print("}", end="")

    def print_sorted_tuple(t: tuple):
        flag = False
        print("(", end="")
        for item in sorted(t, key=choose_key):
            if flag:
                print(", ", end="")
            funcs_dict.get(type(item), print_no_new_line)(item)
            flag = True
        print(")", end="")

    # dict that's used to call appropriate method for each type
    funcs_dict = {
        list: print_sorted_list,
        dict: print_sorted_dict,
        set: print_sorted_set,
        tuple: print_sorted_tuple
    }

    funcs_dict.get(type(obj), print_no_new_line)(obj)
    print("")


if __name__ == '__main__':
    testmod(name='assignment1', verbose=True)
