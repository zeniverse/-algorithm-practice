
from collections import defaultdict
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.extend(arr)

counter = defaultdict(int)
left = 0
right = 0
res = 0

counter[c] += 1

for right in range(len(arr)):
    counter[arr[right]] += 1

    if right >= k - 1:
        res = max(res, len(counter))

        counter[arr[left]] -= 1

        if counter[arr[left]] == 0:
            del counter[arr[left]]
        left += 1

print(res)

