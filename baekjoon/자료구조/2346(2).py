from collections import deque
import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

for i, num in enumerate(arr, start=1):
    arr[i - 1] = (i, num)

d = deque(arr)
res = []

while d:
    index, paper = d.popleft()
    res.append(index)

    if paper > 0:
        d.rotate(-(paper - 1))
    elif paper < 0:
        d.rotate(-paper)

print(*res)
