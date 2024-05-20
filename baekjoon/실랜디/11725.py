from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)

q = deque()
q.append(1)

while q:
    current = q.popleft()

    for v in graph[current]:
        if parent[v] == 0:
            parent[v] = current
            q.append(v)

print('\n'.join(map(str, parent[2:])))