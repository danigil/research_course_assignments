import itertools
import time
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

    >>> for s in zip(range(5), bounded_subsets(range(100), 10000000000000000000)): print(s)
    (0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
    (1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98])
    (2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99])
    (3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97])
    (4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99])

    >>> for s in zip(range(5), bounded_subsets(range(50,150), 103)): print(s)
    (0, [50, 51])
    (1, [50, 52])
    (2, [50, 53])
    (3, [50])
    (4, [51, 52])

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

    if not all([isinstance(item, int) and item >= 0 for item in l]) or not isinstance(num, int) or num <= 0:
        raise Exception
    else:
        l = list(filter(lambda x: x <= num, l))
        l.sort()

        for subset in inner_func(l, num):
            yield subset

def inefficient_bss(l, num):
    for i in range(len(l)):
        for subset in itertools.combinations(l,i):
            if sum(subset) <= num:
                yield subset

if __name__ == '__main__':
    testmod(name='assignment3_ex1', verbose=True)
