import heapq
INF = int(1e9)

N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4

def floyd(graph, N, K):
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    

def solution(N, road, K):

    graph = [[INF] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        graph[i][i] = 0
        

    for i in road:
        a, b, c = i
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)

    floyd(graph, N, K)

    for i in graph[1]:
        print(i)

    return len([i for i in graph[1] if i <= K])
    
print(solution(N, road, K))
