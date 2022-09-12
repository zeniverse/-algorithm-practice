
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

graph = [[1] * n for _ in range(n)]
res = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b or a == k or b == k:
                continue
            if arr[a][b] == arr[a][k] + arr[k][b]:
                graph[a][b] = 0

            elif arr[a][b] > arr[a][k] + arr[k][b]:
                res = -1

if res != -1:
    for i in range(n):
        for j in range(i, n):
            if graph[i][j]:
                res += arr[i][j]

print(res)
