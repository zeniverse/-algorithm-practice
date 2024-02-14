import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for e in graph[now]:
            cost = dist + e[1]

            if cost < distance[e[0]]:
                distance[e[0]] = cost
                heapq.heappush(queue, (cost, e[0]))

dijkstra(x)
res = []
for i in range(1, n + 1):
    if distance[i] == k:
        res.append(i)

if not res:
    print(-1)
else:
    for i in res:
        print(i)