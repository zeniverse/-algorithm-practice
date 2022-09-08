
import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

def get_distance(x1, y1, x2, y2):
    return (abs(x1 - x2)**2 + abs(y1 - y2)**2) ** 0.5

n, w = map(int, input().split())
m = float(input())

pos = [[0, 0]]
nodes = [[] for _ in range(n + 1)]

for _ in range(n):
    x, y = map(int, input().split())
    pos.append([x, y])

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        dist = get_distance(pos[i][0], pos[i][1], pos[j][0], pos[j][1])

        if dist <= m:
            nodes[i].append((j, dist))
            nodes[j].append((i, dist))

for _ in range(w):
    a, b = map(int, input().split())
    nodes[a].append((b, 0))
    nodes[b].append((a, 0))


def dijkstra():
    distance = [INF] * (n + 1)
    distance[1] = 0

    queue = []
    heapq.heappush(queue, (0, 1))

    while queue:
        cost, now = heapq.heappop(queue)

        if distance[now] < cost:
            continue

        for i in nodes[now]:
            next_cost = cost + i[1]

            if next_cost < distance[i[0]]:
                distance[i[0]] = next_cost
                heapq.heappush(queue, (next_cost, i[0]))

    return int(distance[n] * 1000)

print(dijkstra())