from collections import deque
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.extend(arr)

counter = [0] * (d + 1)
res = 0
count = 0
window = deque()

for i, v in enumerate(arr):
    window.append(v)
    counter[v] += 1

    if counter[v] == 1:
        count += 1

    if i < k -1:
        continue

    if counter[c] == 0:
        res = max(res, count + 1)
    else:
        res = max(res, count)

    num = window.popleft()
    counter[num] -= 1
    if counter[num] == 0:
        count -= 1

print(res)

