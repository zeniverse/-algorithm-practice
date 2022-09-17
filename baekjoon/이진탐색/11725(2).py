
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        x = queue.popleft()

        for e in adj[x]:
            if visited[e] == -1:
                visited[e] = x
                queue.append(e)

bfs(1)

for i in range(2, n + 1):
    print(visited[i])