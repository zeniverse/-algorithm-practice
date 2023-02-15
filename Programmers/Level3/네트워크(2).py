

def solution(n, computers):
    res = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            bfs(n, computers, i, visited)
            res += 1
    return res

def bfs(n, computers, com, visited):
    queue = [com]

    while queue:
        com = queue.pop(0)
        visited[com] = True

        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if not visited[connect]:
                    queue.append(connect)

    

n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))

