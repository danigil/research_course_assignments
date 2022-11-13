from doctest import testmod
from typing import Callable


def lastcall(func: Callable,d={}) -> Callable:
    """
    lastcall

    function thats meant to be used as a decorator,
    it remembers return values of calls to the parameter function with specific values

    lastcall takes advantage of the fact that default arguments are created once per function and not for every call.

    #Check that type of args are distinct (the wrapper doesn't count f1(2) and f1(x=2) as the same call)

        >>> f1(2)
        4

        >>> f1(x=2)
        4

        >>> f1(2)
        I already told you that the answer is 4!

        >>> f1(x=2)
        I already told you that the answer is 4!

        >>> f2(2,'a')
        aa

        >>> f2(2,'a')
        I already told you that the answer is aa!

        >>> f2(2,y='a')
        aa

        >>> f2(x=2,y='a')
        aa
    """

    def wrapper(*args, **kwargs):
        #print(d)
        key = (func,tuple(args), tuple(kwargs.items()))

        if key in d:
            print(f"I already told you that the answer is {d[key]}!")
        else:
            ret = func(*args, **kwargs)
            d[key] = ret
            print(ret)

    return wrapper


@lastcall
def f1(x: int):
    return x ** 2

@lastcall
def f2(x: int, y: str):
    return y * x



if __name__ == '__main__':
    testmod(name='assignment2_ex2', verbose=True)
