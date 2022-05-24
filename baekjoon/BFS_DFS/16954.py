from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append((7, 0))

    count = 0

    while queue:
        queueLen = len(queue)

        # 벽이 밀릴때 마다 visited 리스트를 초기화 해준다.
        visited = [[False] * 8 for _ in range(8)]

        for _ in range(queueLen):
            x, y = queue.popleft()

            if arr[x][y] == '#':
                continue

            if (x, y) == (0, 7):
                return 1

            for i in directions:
                nx = x + i[0]
                ny = y + i[1]

                if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
                    continue

                if not visited[nx][ny] and arr[nx][ny] != '#':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    

        # 체스판 아래로 밀어내고 새로운 빈칸 제일 윗줄에 추가하기
        arr.pop()
        arr.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])


        count += 1

        # 9초 이후에는 벽이 모두 아래로 밀려났기 때문에
        # 무조건 도착지까지 도착 가능함
        if count == 9:
            return 1

    return 0


arr = deque(list(input().rstrip()) for _ in range(8))
directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

print(bfs())

