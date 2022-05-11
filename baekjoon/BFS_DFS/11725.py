import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
parent = [-1] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[b].append(a)
    adj[a].append(b)

def dfs(v):
    for e in adj[v]:
        if parent[e] == -1:
            parent[e] = v
            dfs(e)

dfs(1)

for i in range(2, n + 1):
    print(parent[i])