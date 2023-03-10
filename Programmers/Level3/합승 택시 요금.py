import heapq

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    # 다익스트라
    MAX = 100000 * n + 1
    min_dis = [[MAX for _ in range(n + 1)] for _ in range(n + 1)]

    for start in range(1, n + 1):
        hq = [(0, start)]

        while hq:
            cost, now = heapq.heappop(hq)

            if min_dis[start][now] <= cost:
                continue
            min_dis[start][now] = cost

            for next, next_cost in graph[now]:
                if min_dis[start][next] <= next_cost + cost:
                    continue
                heapq.heappush(hq, (next_cost + cost, next))
            

    # 분기점을 기준으로 총 비용을 계산
    res = MAX * 2
    
    for i in range(1, n + 1):
        total = min_dis[s][i] + min_dis[i][a] + min_dis[i][b]
        res = min(res, total)

    return res

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))