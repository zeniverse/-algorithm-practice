

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n

def dfs(v):
    for i in range(n):
        if not visited[i] and graph[v][i] == 1:
            visited[i] = True
            dfs(i)

for num in range(n):
    dfs(num)

    for j in range(n):
        if visited[j]:
            print(1, end=' ')
        else:
            print(0, end=' ')

    print()
    visited = [False] * n