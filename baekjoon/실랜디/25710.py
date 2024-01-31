from itertools import combinations_with_replacement
from collections import Counter

n = int(input())
arr = Counter(map(int, input().split()))

res = 0
for i, j in combinations_with_replacement(arr, 2):
    if i != j or arr[i] > 1:
        res = max(res, sum(map(int, str(i * j))))

print(res)