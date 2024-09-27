import itertools

arr = [[80,20],[50,40],[30,10]]
nPr = itertools.permutations(arr, len(arr))
print(len(arr),list(nPr))