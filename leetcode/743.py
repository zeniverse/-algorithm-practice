from collections import defaultdict
import heapq


def networkDelayTime(times, n: int, k: int) -> int:
    INF = int(1e9)

    graph = [[] for _ in range(n + 1)]

    for i in times:
        a, b, c = map(int, i)
        graph[a].append((b, c))

    def dijkstra(graph, start):
        N = len(graph)
        dist = [INF] * N

        q = []
        heapq.heappush(q, (0, start))
        dist[start] = 0

        while q:
            acc, cur = heapq.heappop(q)

            if dist[cur] < acc:
                continue

            for adj, d in graph[cur]:
                cost = acc + d
                if cost < dist[adj]:
                    dist[adj] = cost
                    heapq.heappush(q, (cost, adj))

        return dist
    
    dist = dijkstra(graph, k)
    m = 0
    for d in range(1, len(dist)):
        if INF <= dist[d]:
            return -1
        m = max(m, dist[d])
    return m


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))