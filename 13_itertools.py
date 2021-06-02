import itertools


l1 = itertools.chain([1, 2, 3], [4, 5], [6, 7])
print(list(l1))


l2 = itertools.filterfalse(lambda x: len(x) < 5, ['hello', 'i', 'write', 'cool', 'code'])
print(list(l2))


l3 = itertools.permutations('password', 4)
print(list(l3))