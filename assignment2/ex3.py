from doctest import testmod


class List(list):
    """
    List
    this class extends list's functionality to allow getting info like this: list[1,2,3] instead of list[1][2][3]
    everything else functions the same as well as list[1].

    !!!   IMPORTANT   !!! the [] operator is used here for getting data from nested lists only.

    >>> mylist = List([[[4,5,6],7],1,2])
    >>> print(mylist[0,0,1])
    5

    >>> print(mylist[0])
    [[4, 5, 6], 7]

    >>> print(mylist[0,1])
    7
    """

    #initialize list as always
    def __init__(self, input):
        super().__init__(input)

    """
    if item is an integer:  ie. call looked like: array[5] then return element from the super
    otherwise recurse with the inner array member through the leftmost index from the tuple
    and the rest of the tuple as indexes.
    """
    def __getitem__(self, item):
        def nested_return(l: list, index):
            if isinstance(index, tuple):
                if len(index) == 1:
                    return l[index[0]]
                else:
                    return nested_return(l[index[0]], index[1:])

            elif isinstance(index, int):
                return super().__getitem__(index)

        return nested_return(self,item)

if __name__ == '__main__':
    testmod(name='assignment2_ex3', verbose=True)