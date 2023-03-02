import heapq
INF = int(1e9)

def dijkstra(start, graph, n):
    distance = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue, [0, start])
    distance[start] = 0

    while queue:
        dist, current = heapq.heappop(queue)

        if distance[current] < dist:
            continue

        for i in graph[current]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, [cost, i[0]])

    return distance


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]

    for i in range(len(edge)):
        a, b = edge[i]
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    distance = dijkstra(1, graph, n)[1:]
    max_ = max(distance)

    res = 0

    for i in distance:
        if i == max_:
            res += 1

    return res

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))