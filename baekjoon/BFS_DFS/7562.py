from collections import deque
import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')

directions = [(1, 2), (1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while True:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            print(visited[x][y])
            break

        for i in directions:
            nx = x + i[0]
            ny = y + i[1]

            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            if not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1


for _ in range(int(input())):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    visited = [[0] * l for _ in range(l)]

    bfs(start_x, start_y)