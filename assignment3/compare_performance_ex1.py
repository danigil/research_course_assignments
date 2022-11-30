from ex1 import bounded_subsets
from typing import List
from time import perf_counter

def bounded_subsets_inefficient(l: List[int], num: int):
    def powerset(l):
        if len(l) <= 1:
            yield l
            yield []
        else:
            for item in powerset(l[1:]):
                yield [l[0]] + item
                yield item


    for subset in powerset(l):
        if sum(subset) <= num:
            yield list(subset)

def compare(input_list, input_bound):
    print(f'input_list: {input_list}, input_bound: {input_bound}')

    start = perf_counter()
    list(bounded_subsets(input_list, input_bound))
    my_func = perf_counter() - start
    print(f'my func elapsed time: {my_func}')

    start = perf_counter()
    list(bounded_subsets_inefficient(input_list, input_bound))
    inefficient_func = perf_counter() - start
    print(f'inefficient func elapsed time: {inefficient_func}')

    print(f'my func is faster: {my_func < inefficient_func}')
    print("")

if __name__ == '__main__':
    """
        Here we compare runtime between my function and a generator that generates 
        all subsets and yields when the sum of the subset is less than the given bound
        
        Note: if we pass a bound such that it is greater than the sum of the biggest subset, 
        my function will calculate all subsets anyway, as it has more overhead, my function 
        in these cases will actually perform worse.
        on the other hand, in cases where we are actually binding the sum with a non trivial bound my function 
        will indeed perform better compared with a function that generates all subsets.
        
        for example: with inputs [1]*20 and a bound of 2 my function is 100 times quicker since it doesnt calculate
        unnecessary calculations.
        
        both functions are O(2^n) worst-case where n is the length of the given array
        even so - for example when running compare with [1]*30 and a bound of 2 
        out of curiosity i decided to let it finish the calculation to see the difference
        my function stops within miliseconds, while the inefficient function stopped after 590 seconds
        or 10 minutes. This is a substantial improvement.
        
        
    """
    compare([1] * 20, 2)

    compare([1,2,3,4], 10)

    compare([1] * 30, 2)



