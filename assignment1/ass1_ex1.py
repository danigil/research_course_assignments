from doctest import testmod


def f1(x: int, y: int, z):
    return x + y + z


def safe_call(func, **kwargs):
    """
    safe_call
    receives function, args for that function and calls the function
    with those args if they match the annotations, otherwise throws exception.

    ##Good Cases (Shouldn't throw)
        >>> safe_call(f1,x=5,y=5,z=5)
        15

        >>> safe_call(f1,x=5,y=5,z=5.7)
        15.7

    ##Bad Cases (Should throw)
        #mismatching annotation
        >>> safe_call(f1,x=5.0,y="hello",z='z')
        Traceback (most recent call last):
         ...
        Exception

        #incorrect order
        >>> safe_call(f1,x="1",y=1,z=1)
        Traceback (most recent call last):
         ...
        Exception
     """

    for arg, annot in zip(func.__annotations__.values(), (type(val) for val in kwargs.values())):
        if arg is not annot:
            raise Exception

    return func(**kwargs)

if __name__ == '__main__':
    testmod(name='assignment1_ex1', verbose=True)