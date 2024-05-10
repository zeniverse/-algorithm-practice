from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0

for a, b, c in combinations(range(m), 3):
    tmp = 0
    for i in range(n):
        tmp += max(arr[i][a], arr[i][b], arr[i][c])
    
    res = max(res, tmp)

print(res)