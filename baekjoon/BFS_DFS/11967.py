from collections import defaultdict, deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
info = defaultdict(list)
visited = [[False] * n for _ in range(n)]
lights = [[0] * n for _ in range(n)]

# defaultdict를 통해 불을 키고 끌 수 있는 방의 묶음을 담아준다
for _ in range(m):
    a, b, c, d = map(int, input().split())
    info[(a - 1, b - 1)].append((c - 1, d - 1))


def bfs():
    queue = deque()
    queue.append((0, 0))

    visited[0][0] = 1
    lights[0][0] = 1
    
    count = 1

    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 불을 킬 수 있는 곳 찾아서 불 키기
        for a_, b_ in info[(x, y)]:
            if not lights[a_][b_]:
                lights[a_][b_] = 1
                count += 1

                # 불을 켤 수 있는 곳과 인접한 곳이 방문처리 된 곳이라면
                # 다시 한번 큐에 담아 준다
                # (다시 한번 방문해서 queue에 담아줄 내용이 변경됐는지 확인해야한다)
                for i in range(4):
                    na = a_ + dx[i]
                    nb = b_ + dy[i]

                    if na < 0 or na >= n or nb < 0 or nb >= n:
                        continue

                    if visited[na][nb]:
                        queue.append((na, nb))

        # 현재 위치에서 상하좌우로 이동해, 불켜져있다면 queue에 담아준다 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and lights[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return count

print(bfs())
