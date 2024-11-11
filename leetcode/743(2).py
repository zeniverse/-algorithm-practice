from collections import defaultdict
import heapq


def networkDelayTime(times, n: int, k: int) -> int:
    graph = defaultdict(list)

    for i in times:
        graph[i[0]].append((i[2], i[1]))

    costs = {}
    queue = []
    heapq.heappush(queue, (0, k))

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)

        if cur_node not in costs:
            costs[cur_node] = cur_cost

            for cost, next_node in graph[cur_node]:
                next_cost = cur_cost + cost
                heapq.heappush(queue, (next_cost, next_node))

    for node in range(1, n + 1):
        if node not in costs:
            return -1
        
    return max(costs.values())


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))