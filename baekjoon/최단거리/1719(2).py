
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
res = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

    res[a][b] = b
    res[b][a] = a

for i in range(1, n + 1):
    graph[i][i] = 0
    res[i][i] = INF

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                res[a][b] = res[a][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if res[i][j] == INF:
            res[i][j] = '-'

for i in res[1:]:
    print(*i[1:])