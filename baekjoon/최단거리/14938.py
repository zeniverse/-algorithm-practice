
import heapq, sys
input = sys.stdin.readline

INF = int(1e9)

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))



def dijkstra(start, distance):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    ans = 0

    for i in range(1, len(distance)):
        if distance[i] != INF and distance[i] <= m:
            ans += items[i - 1]

    return ans

res = 0
for i in range(1, n + 1):
    distance = [INF] * (n + 1)
    tmp = dijkstra(i, distance)
    res = max(res, tmp)

print(res)