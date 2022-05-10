from collections import deque

def bfs():
    queue = deque()
    queue.append((1, 0)) # (화면에 있는 이모지 개수, 클립보드 이모지 개수)
    distance[1][0] = 0

    while queue:
        s, c = queue.popleft()

        # 클립보드에 이모지를 복사한 경우
        if distance[s][s] == -1:
            distance[s][s] = distance[s][c] + 1
            queue.append((s, s))

        # 클립보드에 있는 이모티콘을 화면에 붙여넣기 한 경우
        if s + c <= n and distance[s + c][c] == -1:
            distance[s + c][c] = distance[s][c] + 1
            queue.append((s + c, c))

        # 화면에 있는 이모티콘을 하나 삭제한 경우
        if s - 1 >= 0 and distance[s - 1][c] == -1:
            distance[s - 1][c] = distance[s][c] + 1
            queue.append((s - 1, c))


n = int(input())
distance = [[-1] * (n + 1) for _ in range(n + 1)]

bfs()
ans = -1

for i in range(1, n + 1):
    if distance[n][i] != -1:
        if ans == -1 or ans > distance[n][i]:
            ans = distance[n][i]

print(ans)