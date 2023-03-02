from collections import deque

def bfs(graph, start, distances, n):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        now = queue.popleft()

        for e in graph[now]:
            if not visited[e]:
                visited[e] = True
                queue.append(e)
                distances[e] = distances[now] + 1


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    for i in range(len(edge)):
        a, b = edge[i]
        graph[a].append(b)
        graph[b].append(a)

    distances = [0] * (n + 1)
    bfs(graph, 1, distances, n)
    max_ = max(distances)

    res = 0

    for i in distances:
        if i == max_:
            res += 1

    return res

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))