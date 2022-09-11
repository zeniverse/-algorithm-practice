
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(n):
    res = 0
    for j in range(n):
        if not graph[i][j] and not graph[j][i]:
            res += 1

    print(res - 1)