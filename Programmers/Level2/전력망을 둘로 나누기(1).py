import sys

n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

def solution(n, wires):
    res = sys.maxsize

    def dfs(v):
        visited[v] = True

        for e in adj[v]:
            if not visited[e]:
                dfs(e)

    for i in range(len(wires)):
        tmp = wires[:i] + wires[i + 1:]
        print(tmp)
        adj = [[] for _ in range(n + 1)]

        for v1, v2 in tmp:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visited = [False] * (n + 1)
        for i in range(1, n + 1):
            dfs(i)
            cnt = visited.count(True)
            res = min(abs(cnt -(n - cnt) ), res)
            break

    return res

print(solution(n, wires))