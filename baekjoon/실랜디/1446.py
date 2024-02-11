import heapq

INF = int(1e9)

def dijkstra(start):
    queue = []

    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if dist > distance[now]:
            continue

        for a, b in graph[now]:
            cost = dist + b

            if cost < distance[a]:
                distance[a] = cost
                heapq.heappush(queue, (cost, a))


n, d = map(int, input().split())
graph = [[] for _ in range(d + 1)]
distance = [INF] * (d + 1)

for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    s, e, l = map(int, input().split())
    if e > d:
        continue
    graph[s].append((e, l))

dijkstra(0)
print(distance[d])