from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    res = 0
    start_x, start_y = 0, 0
    l_x, l_y = 0, 0
    e_x, e_y = 0, 0
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start_x = i
                start_y = j
            elif maps[i][j] == 'L':
                l_x = i
                l_y = j
            elif maps[i][j] == 'E':
                e_x = i
                e_y = j

                
    def bfs(x, y, a, b):
        n = len(maps)
        m = len(maps[0])

        visited = [[-1] * m for _ in range(n)]
        visited[x][y] = 0
        queue = deque()
        queue.append((x, y))

        while queue:
            x_, y_ = queue.popleft()

            if x_ == a and y_ == b:
                return visited[x_][y_]
            
            for i in range(4):
                nx = x_ + dx[i]
                ny = y_ + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if maps[nx][ny] != 'X'and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x_][y_] + 1
                    queue.append((nx, ny))

        return -1

    lever = bfs(start_x, start_y, l_x, l_y)
    if lever == -1:
        return -1
    
    exit = bfs(l_x, l_y, e_x, e_y)
    
    return lever + exit if exit != -1 else -1


maps= ["XXXXL", "XOOSX", "XXXXX", "XXXOO", "EXXXX", "XXXXX"]
print(solution(maps))