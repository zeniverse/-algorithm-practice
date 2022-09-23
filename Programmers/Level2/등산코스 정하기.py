

from collections import defaultdict
import heapq
INF = int(1e9)

n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]

def solution(n, paths, gates, summits):

    def get_min_intensity():
        queue = []
        visited = [INF] * (n + 1)

        for gate in gates:
            heapq.heappush(queue, (0, gate))
            visited[gate] = 0

        while queue:
            intensity, node = heapq.heappop(queue)


            if node in summits_set or intensity > visited[node]:
                continue

            for next_node, cost in graph[node]:
                new_intensity = max(cost, intensity)

                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heapq.heappush(queue, (new_intensity, next_node))

                    
        res = [0, INF]

        for summit in summits:
            if visited[summit] < res[1]:
                res[0] = summit
                res[1] = visited[summit]

        return res


    summits.sort()
    summits_set = set(summits)

    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    return get_min_intensity()

print(solution(n, paths, gates, summits))