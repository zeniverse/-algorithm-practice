from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [deque([0] * 20) for _ in range(n)]

for _ in range(m):
    arr = list(map(int, input().split()))

    if arr[0] == 1:
        train[arr[1] - 1][arr[2] - 1] = 1
    elif arr[0] == 2:
        train[arr[1] - 1][arr[2] - 1] = 0
    elif arr[0] == 3:
        train[arr[1] - 1].rotate(1)
        train[arr[1] - 1][0] = 0
    else:
        train[arr[1] - 1].rotate(-1)
        train[arr[1] - 1][19] = 0

res = []

for i in train:
    if i not in res:
        res.append(i)

print(len(res))