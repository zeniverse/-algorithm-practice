import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

v, e = map(int, input().split())
k = int(input())

distance = [INF] * (v + 1)
graph = [[] for _ in range(v + 1)] 

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

queue = []
heapq.heappush(queue, (0, k))
distance[k] = 0

while queue:
    dist, current = heapq.heappop(queue)

    if dist > distance[current]:
        continue

    for i in graph[current]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(queue, (cost, i[0]))

for i in range(1, len(distance)):
    print("INF" if distance[i] == INF else distance[i])