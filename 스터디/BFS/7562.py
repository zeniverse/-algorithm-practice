# 처음에 다른 문제들 처럼 n의 크기만큼 arr로 만들어주고 시작해야 하는 줄 알고 헷갈림.
# 그냥 처음 시작점과 끝나는점만 기록해주고 얼마만큼 이동후에 도착하는지 출력해주면 된다.


from collections import deque

directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2) ,(-1, -2)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            return visited[x][y]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


for _ in range(int(input())):
    n = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    visited = [[-1] * n for _ in range(n)]
    print(bfs(start_x, start_y))