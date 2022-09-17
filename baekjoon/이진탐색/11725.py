
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(v):
    for e in adj[v]:
        if visited[e] == -1:
            visited[e] = v
            dfs(e)

dfs(1)

for i in range(2, n + 1):
    print(visited[i])
