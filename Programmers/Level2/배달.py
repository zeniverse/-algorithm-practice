import heapq
INF = int(1e9)

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

def dijkstra(adj, distance):
    queue = []
    heapq.heappush(queue, (0, 1))
    distance[1] = 0

    while queue:
        dist, current = heapq.heappop(queue)

        if distance[current] < dist:
            continue
        
        for i in adj[current]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


def solution(N, road, K):

    distance = [INF] * (N + 1)
    adj = [[] for i in range(N + 1)]

    for i in road:
        a, b, c = i
        adj[a].append((b, c))
        adj[b].append((a, c))

    dijkstra(adj, distance)

    return len([i for i in distance if i <= K])
    
print(solution(N, road, K))
