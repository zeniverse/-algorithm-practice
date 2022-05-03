n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def dfs(v):
    global count

    visited[v] = True
    count += 1

    for e in adj[v]:
        if not visited[e]:
            dfs(e)

dfs(1)
print(count - 1)

