from collections import deque
import sys
input = sys.stdin.readline

ans = []

def dfs(v):
    visited[v] = True

    ans.append(v)
    
    for e in adj[v]:
        if not visited[e]:
            visited[e] = True
            dfs(e)


n = int(input())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
order = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

res = list(map(int, input().split()))

for i in range(len(res)):
    order[res[i]] = i

for i in range(1, len(adj)):
    adj[i] = sorted(adj[i], key=lambda x : order[x])

dfs(1)

if ans == res:
    print(1)
else:
    print(0)
