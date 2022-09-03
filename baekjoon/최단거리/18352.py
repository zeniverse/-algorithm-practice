import heapq, sys
input = sys.stdin.readline

INF = int(1e9)

n, m, k, x = map(int, input().split())
edges = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append((b, 1))

distance = [INF] * (n + 1)

queue = []
heapq.heappush(queue, (0, x))
distance[x] = 0

while queue:
    dist, current = heapq.heappop(queue)

    if distance[current] < dist:
        continue

    for i in edges[current]:
        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(queue, (cost, i[0]))

res = [i for i in range(len(distance)) if distance[i] == k]

if not res:
    print(-1)
else:
    [print(i) for i in res]