
def solution(n, s, a, b, fares):
    MAX = 100000 * n + 1

    dist = [[MAX for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for x, y, c in fares:
        dist[x - 1][y - 1] = c
        dist[y - 1][x - 1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[j][k] > dist[j][i] + dist[i][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]

    res = MAX * 2
    for i in range(n):
        res = min(res, dist[s - 1][i] + dist[i][a - 1] + dist[i][b - 1])

    return res

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))