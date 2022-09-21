from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]

def dfs(x):
    visited[x] = True
    print(x, end= ' ')
    for e in adj[x]:
        if not visited[e]:
            dfs(e)

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True
    print(x, end = ' ')

    while queue:
        a = queue.popleft()

        for e in adj[a]:
            if not visited[e]:
                visited[e] = True
                print(e, end = ' ')
                queue.append(e)


for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for e in adj:
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)