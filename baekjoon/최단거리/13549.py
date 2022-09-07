from collections import deque


n, k = map(int, input().split())
max = 100_001
visited = [-1] * max


def bfs(n, k):
    queue = deque([n])
    visited[n] = 0

    while queue:
        now_pos = queue.popleft()

        if now_pos == k:
            return visited[now_pos]

        if now_pos * 2 < max and visited[now_pos * 2] == -1:
            visited[now_pos * 2] = visited[now_pos]
            queue.appendleft(now_pos * 2)

        if now_pos + 1 < max and visited[now_pos + 1] == -1:
            visited[now_pos + 1] = visited[now_pos] + 1
            queue.append(now_pos + 1)

        if 0 <= now_pos -1 < max and visited[now_pos - 1] == -1:
            visited[now_pos - 1] = visited[now_pos] + 1
            queue.append(now_pos - 1)

print(bfs(n, k))