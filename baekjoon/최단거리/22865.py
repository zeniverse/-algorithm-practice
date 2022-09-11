import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
friends = list(map(int, input().split()))
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(graph, start):
    distance = [INF] * (n + 1)
    distance[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

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

max_size = 0
res = 0

distance_a = dijkstra(graph, friends[0])
distance_b = dijkstra(graph, friends[1])
distance_c = dijkstra(graph, friends[2])

for i in range(1, n + 1):
    if max_size < min(distance_a[i], distance_b[i], distance_c[i]):
        max_size = min(distance_a[i], distance_b[i], distance_c[i])
        res = i

print(res)
