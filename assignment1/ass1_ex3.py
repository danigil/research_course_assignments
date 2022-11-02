from doctest import testmod


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
    testmod(name='assignment1_ex3', verbose=True)