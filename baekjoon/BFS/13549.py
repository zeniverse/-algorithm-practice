from collections import deque

def bfs(v):
    queue = deque([v])
    arr[v] = 0

    while queue:
        now_pos = queue.popleft()

        if now_pos == k:
            return arr[now_pos]

        if now_pos * 2 < max and arr[now_pos * 2] == -1:
            arr[now_pos * 2] = arr[now_pos]
            queue.appendleft(now_pos * 2)

        if now_pos + 1 < max and arr[now_pos + 1] == -1:
            arr[now_pos + 1] = arr[now_pos] + 1
            queue.append(now_pos + 1)

        if 0 <= now_pos -1 < max and arr[now_pos - 1] == -1:
            arr[now_pos - 1] = arr[now_pos] + 1
            queue.append(now_pos - 1)

n, k = map(int, input().split())
max = 100_001
arr = [-1] * max

print(bfs(n))