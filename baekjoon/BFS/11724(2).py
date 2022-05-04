import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(v):
    visited[v] = True

    for e in adj[v]:
        if not visited[e]:
            dfs(e)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)