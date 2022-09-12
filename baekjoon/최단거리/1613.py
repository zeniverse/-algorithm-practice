import sys
input = sys.stdin.readline

INF = int(1e9)

n, k = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

s = int(input())
for _ in range(s):
    a, b = map(int, input().split())

    if graph[a][b] != INF:
        print(-1)
    else:
        if graph[b][a] != INF:
            print(1)
        else:
            print(0)
