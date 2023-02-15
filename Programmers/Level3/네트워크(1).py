

def solution(n, computers):
    res = 0
    adj = [[] for _ in range(n)]
    visited = [False] * n

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                adj[i].append(j)

    def dfs(v):
        visited[v] = True

        for e in adj[v]:
            if not visited[e]:
                dfs(e)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            res += 1

    return res
    

n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))

