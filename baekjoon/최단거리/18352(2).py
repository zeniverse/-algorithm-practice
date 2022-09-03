from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, k, x = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)

distance = [0] * (n + 1)
visited = [False] * (n + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    res = []

    while queue:
        now = queue.popleft()

        for e in edges[now]:
            if not visited[e]:
                visited[e] = True
                distance[e] = distance[now] + 1
                queue.append(e)

                if distance[e] == k:
                    res.append(e)

    if res:
        res.sort()
        [print(i) for i in res]
    else:
        print(-1)

bfs(x)

