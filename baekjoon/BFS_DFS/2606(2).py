import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
count = 0

def dfs(v):
    global count
    for e in adj[v]:
        if not visited[e]:
            visited[e] = True
            count += 1
            dfs(e)


adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n + 1)
visited[1] = True
dfs(1)

print(count)