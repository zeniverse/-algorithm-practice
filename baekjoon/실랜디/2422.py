from itertools import combinations

n, m = map(int, input().split())
arr = [[False] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = True
    arr[b - 1][a - 1] = True

res = 0

for combi in combinations(range(n), 3):
    if arr[combi[0]][combi[1]] or arr[combi[0]][combi[2]] or arr[combi[1]][combi[2]]:
        continue
    res += 1

print(res)





