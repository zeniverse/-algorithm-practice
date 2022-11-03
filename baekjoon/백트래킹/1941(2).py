from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

lst = [list(input().rstrip()) for _ in range(5)]
arr = [(i, j) for i in range(5) for j in range(5)]
res = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check_count(combi):
    count = 0
    for x, y in combi:
        if lst[x][y] == 'S':
            count += 1

    return True if count >= 4 else False
    

def check_pos(combi):
    visited = [False] * 7
    queue = deque()
    queue.append(combi[0])

    visited[0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx, ny) in combi:
                idx = combi.index((nx, ny))
                if not visited[idx]:
                    visited[idx] = True
                    queue.append((nx, ny))

    return False if False in visited else True


# combinations를 통해 좌표들의 조합 7개를 찾아낸다
for combi in combinations(arr, 7):
    # 좌표들의 위치에 'S' 이다솜파가 몇명인지 확인
    if check_count(combi):
        # 좌표들이 모두 인접해있는지 확인
        if check_pos(combi):
            res += 1

print(res)

