import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, e = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

node1, node2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in adj[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance

one = dijkstra(1)
n1 = dijkstra(node1)
n2 = dijkstra(node2)

res = min(one[node1] + n1[node2] + n2[n], one[node2] + n2[node1] + n1[n])

if res < INF:
    print(res)
else:
    print(-1)
