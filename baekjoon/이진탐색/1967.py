
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
adj = [[] for _ in range(n + 1)]



def dijkstra(start, distance):

    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in adj[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    


for _ in range(n - 1):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

distance = [INF] * (n + 1)
dijkstra(1, distance)

one = max(distance[1:])
index_one = distance.index(one)

distance = [INF] * (n + 1)
dijkstra(index_one, distance)

two = max(distance[1:])
print(two)

