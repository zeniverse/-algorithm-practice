from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()

        for e in adj[v]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)