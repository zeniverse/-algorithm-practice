from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    oil = []
    answer = [0] * m

    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        count = 1
        oil_y = {y}

        while queue:
            x, y = queue.popleft()
            
            for i in directions:
                nx = x + i[0]
                ny = y + i[1]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        count += 1
                        oil_y.add(ny)

        return (oil_y, count)
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                oil.append(bfs(i, j))

    for o, cnt in oil:
        for y in o:
            answer[y] += cnt


    return max(answer)

land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
print(solution(land))