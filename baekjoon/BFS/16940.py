from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    visited = [False] * (n + 1)

    queue = deque([v])
    visited[v] = True
    ans = [1]

    while queue:
        v = queue.popleft()

        for e in adj[v]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True
                ans.append(e)

    return ans


n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

res = list(map(int, input().split()))
order = [0] * (n + 1)

for i in range(len(res)):
    order[res[i]] = i

for i in range(1, len(adj)):
    adj[i] = sorted(adj[i], key=lambda x : order[x])

ans = bfs(1)

if ans == res:
    print(1)
else:
    print(0)