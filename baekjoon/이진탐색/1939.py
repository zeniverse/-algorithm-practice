from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

def bfs(v):
    visited = [False] * (n + 1)
    
    queue = deque([start_node])
    visited[start_node] = True

    while queue:
        x = queue.popleft()

        for y, weight in adj[x]:
            if not visited[y] and weight >= v:
                visited[y] = True
                queue.append(y)
                
    return visited[end_node]

start = 1000000000
end = 1

for _ in range(m):
    a, b, c = map(int, input().split())

    adj[a].append((b, c))
    adj[b].append((a, c))

    start = min(start, c)
    end = max(end, c)

start_node, end_node = map(int, input().split())

res = start
while start <= end:
    mid = (start + end) // 2

    if bfs(mid):
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)
