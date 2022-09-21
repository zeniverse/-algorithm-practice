
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

def bfs(v):
    visited = [False] * (n + 1)
    visited[v] = True
    count = 0

    queue = deque([v])

    while queue:
        x = queue.popleft()

        for e in adj[x]:
            if not visited[e]:
                visited[e] = True
                count += 1
                queue.append(e)

    return count

for _ in range(m):
    a, b = map(int, input().split())
    adj[b].append(a)

res = []
max_ = 0
for i in range(1, n + 1):
    tmp = bfs(i)

    if max_ < tmp:
        max_ = tmp
        res = [i]
    elif max_ == tmp:
        res.append(i)

print(*res)