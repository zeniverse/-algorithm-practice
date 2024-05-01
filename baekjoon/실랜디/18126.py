import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(now, count):
    global res

    visited[now] = True

    for i, j in graph[now]:
        if not visited[i]:
            res = max(res, count + j)
            dfs(i, count + j)

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
res = 0

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dfs(1, 0)

print(res)