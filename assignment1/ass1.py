from doctest import testmod


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


if __name__ == '__main__':
    testmod(name='safe_call', verbose=True)


