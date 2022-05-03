from collections import deque

n, m , v = map(int, input().split())
adj = [[] for _ in range(n + 1)]

def dfs(v):
    visited[v] = True
    print(v, end=" ")

    for i in adj[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])

    while queue:
        v = queue.popleft()

        if not visited[v]:
            visited[v] = True
            print(v, end = " ")

            for i in adj[v]:
                if not visited[i]: 
                    queue.append(i)



for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
