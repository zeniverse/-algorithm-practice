# 순간이동을 했을 경우엔 0초가 흐르기 때문에 현재 visited 값에 + 1을 하지 않고, 현재 visited 값을 바로 넣어준다.
# 그리고 순간이동 한 경우가 0초로 더 빨리 실행되어야 하기때문에(다른 경우보다 높은 우선수위를 갖기 위해서),
# appendleft를 통해서 queue의 제일 앞에 넣어준다.

from collections import deque

n, k = map(int, input().split())
max_ = 100_001
visited = [-1] * max_

def bfs(n, k):
    queue = deque([n])
    visited[n] = 0

    while queue:
        now_pos = queue.popleft()

        if now_pos == k:
            return visited[now_pos]

        if now_pos * 2 < max_ and visited[now_pos * 2] == -1:
            visited[now_pos * 2] = visited[now_pos]
            queue.appendleft(now_pos * 2)

        if now_pos + 1 < max_ and visited[now_pos + 1] == -1:
            visited[now_pos + 1] = visited[now_pos] + 1
            queue.append(now_pos + 1)

        if 0 <= now_pos - 1 < max_ and visited[now_pos - 1] == -1:
            visited[now_pos - 1] = visited[now_pos] + 1
            queue.append(now_pos - 1)

print(bfs(n, k))