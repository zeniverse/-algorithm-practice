import sys, heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    queue = []

    heapq.heappush(queue, (0, start))
    dist[start] = 0

    while queue:
        distance, now = heapq.heappop(queue)

        if dist[now] < distance:
            continue

        for node, cost in graph[now]:
            cost += dist[now]

            if cost < dist[node]:
                dist[node] = cost
                heapq.heappush(queue, (cost, node))


n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dijkstra(c)

count = 0
max_distance = 0

for i in dist:
    if i != 1e9:
        count += 1
        max_distance = max(max_distance, i)

print(count - 1, max_distance)