from itertools import permutations

n = int(input())
k = int(input())
arr = [ input() for _ in range(n)]
res = set()

for per in permutations(arr, k):
    res.add(''.join(per))

print(len(res))