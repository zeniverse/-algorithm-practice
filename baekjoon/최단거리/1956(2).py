import heapq, sys
input = sys.stdin.readline

INF = int(1e9)

v, e = map(int, input().split())
distance = [[INF] * (v + 1) for _ in range(v + 1)]
graph = [[] for _ in range(v + 1)]

queue = []
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    distance[a][b] = c

    heapq.heappush(queue, (c, a, b))

while queue:
    dist, start, end = heapq.heappop(queue)

    if start == end:
        print(dist)
        break

    if distance[start][end] < dist:
        continue

    for i in graph[end]:
        cost = dist + i[0]

        if cost < distance[start][i[1]]:
            distance[start][i[1]] = cost
            heapq.heappush(queue, (cost, start, i[1]))
else:
    print(-1)
