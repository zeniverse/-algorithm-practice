from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

arr = [input().rstrip() for _ in range(8)]
directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
wall = set()
res = 0

for i in range(8):
    for j in range(8):
        if arr[i][j] == '#':
            wall.add((i, j))

visited = set()

queue = deque()
queue.append((7, 0))

while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()

        # 현재 위치에 벽이 존재하는지 확인
        if (x, y) in wall:
            continue
        
        # 도착지에 도착했는지 확인
        if x == 0 and y == 7:
            res = 1
            break

        for i in directions:
            nx = x + i[0]
            ny = y + i[1]

            if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                continue

            if not (nx, ny) in visited and not (nx, ny) in wall:
                visited.add((nx, ny))
                queue.append((nx, ny))


    # 벽이 존재한다면 visited 초기화
    if wall:
        visited = set()

    # x + 1을 해줘서 벽을 이동해주는 과정
    next_wall = set()

    for x, y in wall:
        if x < 7:
            next_wall.add((x + 1, y))
    
    wall = next_wall

print(res)
