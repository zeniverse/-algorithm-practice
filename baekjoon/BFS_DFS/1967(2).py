import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    distance = [INF] * (n + 1)

    distance[start] = 0
    queue = []

    heapq.heappush(queue, [0, start])

    while queue:
        dist, now = heapq.heappop(queue)

        for node, weight in graph[now]:
            total = dist + weight

            if total < distance[node]:
                distance[node] = total
                heapq.heappush(queue, [total, node])
    
    return distance


d = dijkstra(1)
res_d = dijkstra(d.index(max(d[1:])))

print(max(res_d[1:]))