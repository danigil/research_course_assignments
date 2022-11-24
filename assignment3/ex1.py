from typing import List


class bss:
    def __iter__(self, l: List[int], num: int):
        self.list = l
        self.num = num
        return self

    def __next__(self):
        pass

def bounded_subsets(l: List[int], num: int):


    if len(l) >=2:
        with_first = bounded_subsets(l[1:], num - l[0])
        for item in with_first:
            yield [l[0]] + item

        without_first = bounded_subsets(l[1:], num)
        for item in without_first:
            yield item


    elif len(l) == 1 and l[0] <= num:
        yield [l[0]]
        yield []
    else:
        yield []










def bss_wrapper(l: List[int], num: int):
    if not all([isinstance(item, int) for item in l]) or not isinstance(num, int):
        raise Exception
    else:
        l = list(filter(lambda x: x <= num, l))
        l.sort()

        for subset in bounded_subsets(l,num):
            yield subset



def sub_sets(l: List[int]):
    if len(l) <= 1:
        return [l,[]]
    else:
        for arr in sub_sets(l[1:]):
            return [[l[0]]+arr,arr]
        # ret = []
        # for item in l:
        #     new_list = copy.deepcopy(l)
        #     new_list.pop(new_list.index(item))
        #
        #     for arr in sub_sets(new_list):
        #         ret.append(arr)
        #         ret.append(arr+[item])
        #
        # return ret

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

#print(sub_sets([1,2,3,4]))

for s in bounded_subsets([1,2,3],4):
    print(s)

# for s in zip(range(5), bounded_subsets(list(range(100)),1000000000000)):
#     print(s)
