from itertools import combinations
import math

nums = [1, 2, 3, 4]

print(list(combinations(nums, 3)))

n = 1000
arr = [True for i in range(n + 1)]

res = 0

def prime():
    for i in range(2, int(math.sqrt(n)) + 1):
        if arr[i]:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1

prime()

for a, b, c in combinations(nums, 3):
    total = a + b + c

    if arr[total]:
        res += 1

print(res)



