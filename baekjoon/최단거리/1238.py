
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)


n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start, graph):
    distance = [INF] * (n + 1)

    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance

x_distance = dijkstra(x, graph)

res = 0

for i in range(1, n + 1):
    if i != x:
        tmp = dijkstra(i, graph)

        res = max(res, tmp[x] + x_distance[i])

print(res)