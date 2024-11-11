import heapq


def networkDelayTime(times, n: int, k: int) -> int:
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]

    for t in times:
        graph[t[0]].append((t[2], t[1]))

    def dijkstra(graph, start):
        n = len(graph)
        dist = [INF] * n

        queue = []
        heapq.heappush(queue, (0, start))
        dist[start] = 0

        while queue:
            cur_cost, cur_node = heapq.heappop(queue)

            if dist[cur_node] < cur_cost:
                continue

            for cost, next_node in graph[cur_node]:
                next_cost = cur_cost + cost
                if next_cost < dist[next_node]:
                    dist[next_node] = next_cost
                    heapq.heappush(queue, (next_cost, next_node))

        return dist
    
    dist = dijkstra(graph, k)
    res = 0
    for i in range(1, n + 1):
        if dist[i] == INF:
            return -1
        res = max(res, dist[i])

    return res

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))