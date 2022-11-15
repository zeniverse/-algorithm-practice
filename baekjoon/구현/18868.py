import sys
input = sys.stdin.readline

n, m = map(int, input().split())
universe = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(n):
    arr = sorted(universe[i])
    idx = []

    for j in universe[i]:
        idx.append(arr.index(j))

    universe[i] = idx

for i in range(n - 1):
    for j in range(i + 1, n):
        if universe[i] == universe[j]:
            res += 1

print(res)
