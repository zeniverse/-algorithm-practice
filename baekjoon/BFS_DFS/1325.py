from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[b].append(a)

def bfs(v):
    queue = deque([v])
    
    visited = [False] * (n + 1)
    visited[v] = True

    count = 1

    while queue:
        num = queue.popleft()
        for e in adj[num]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True
                count += 1

    return count

res = []
max_value = -1

for i in range(1, n + 1):
    c = bfs(i)

    if max_value < c:
        res = [i]
        max_value = c
    elif c == max_value:
        res.append(i)
        max_value = c

print(*res)