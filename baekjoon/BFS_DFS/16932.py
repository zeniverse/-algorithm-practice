from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# '1'로 묶어주는 BFS
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    visited[x][y] = num
    cnt = 0

    while queue:
        x, y = queue.popleft()
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = num
                queue.append((nx, ny))

    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

num = 1
count_dict = {}
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            count = bfs(i, j)
            count_dict[num] = count
            num += 1
            

res = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            tmp = set()
            # '0'에서 '1'로 바꿀때 본인을 이미 더해서 sum이 1로 시작한다
            sum = 1 
            
            for k in range(4):
                xx = i + dx[k]
                yy = j + dy[k]

                if xx < 0 or xx >= n or yy < 0 or yy >= m:
                    continue
                
                # 근접한 곳에 '1'이 있다면?
                if arr[xx][yy] != 0 and visited[xx][yy] not in tmp:
                    tmp.add(visited[xx][yy])

            # 근접한 '1'의 개수를 다 더하기
            # ex) count_dict[1] = 3 + count_dict[2] = 1
            for l in tmp:
                sum += count_dict[l]

            res = max(res, sum)
print(res)