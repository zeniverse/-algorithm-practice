n, m = map(int, input().split())
adj = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(idx, depth):
    if depth == 4:
        print(1)
        exit(0)
    
    for i in adj[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False



for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)