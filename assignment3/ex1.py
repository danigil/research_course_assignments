from doctest import testmod
from typing import List


def bounded_subsets(l: List[int], num: int):
    """
    >>> for s in bounded_subsets([1, 2, 3], 4): print(s)
    [1, 2]
    [1, 3]
    [1]
    [2]
    [3]
    []

    >>> for s in bounded_subsets([], 4): print(s)
    []

    >>> for s in bounded_subsets([1,2,3,4], 10): print(s)
    [1, 2, 3, 4]
    [1, 2, 3]
    [1, 2, 4]
    [1, 2]
    [1, 3, 4]
    [1, 3]
    [1, 4]
    [1]
    [2, 3, 4]
    [2, 3]
    [2, 4]
    [2]
    [3, 4]
    [3]
    [4]
    []

    >>> for s in bounded_subsets([1, 3, 2, 4], 4): print(s)
    [1, 2]
    [1, 3]
    [1]
    [2]
    [3]
    [4]
    []

    >>> len(list(bounded_subsets(list(range(1,21)), sum(range(1,21)))))
    1048576


    >>> for s in bounded_subsets([1, 'this is not an int, should throw', 3], 4): print(s)
    Traceback (most recent call last):
    ..
    Exception

    >>> for s in bounded_subsets([1, 2, -1], 4): print(s)
    Traceback (most recent call last):
    ..
    Exception

    >>> for s in bounded_subsets([1, 2, 3], 'this is not an int, should throw'): print(s)
    Traceback (most recent call last):
    ..
    Exception

    >>> for s in bounded_subsets([1, 2, 3], -1): print(s)
    Traceback (most recent call last):
    ..
    Exception

    """

    def inner_func(l: List[int], num: int):
        if len(l) >= 2 and num>=0 and l[0] <= num:
            #print(f"with_first, arr: {l[1:]}, num: {num - l[0]}")
            with_first = inner_func(l[1:], num - l[0])
            for item in with_first:
                yield [l[0]] + item

            #print(f"without_first, arr: {l[1:]}, num: {l[0]}")
            without_first = inner_func(l[1:], num)
            for item in without_first:
                yield item


        elif len(l) == 1 and l[0] <= num:
            yield [l[0]]
            yield []
        else:
            yield []

    if not all([isinstance(item, int) and item > 0 for item in l]) or not isinstance(num, int) or num <= 0:
        raise Exception
    else:
        l = list(filter(lambda x: x <= num, l))
        l.sort()

        for subset in inner_func(l, num):
            yield subset

if __name__ == '__main__':
    testmod(name='assignment3_ex1', verbose=True)
    # for s in bounded_subsets([1, 2, 3], 4):
    #     print(s)


