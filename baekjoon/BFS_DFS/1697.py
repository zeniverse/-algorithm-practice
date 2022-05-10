from collections import deque
n, k = map(int, input().split())
max = 100_001
arr = [0] * max


def bfs():
    queue = deque([n])

    while queue:
        now_pos = queue.popleft()

        if now_pos == k:
            return arr[now_pos]

        for next_pos in [now_pos -1, now_pos + 1, now_pos * 2]:
            if 0 <= next_pos < max and not arr[next_pos]:
                arr[next_pos] = arr[now_pos] + 1
                queue.append(next_pos)

print(bfs())

    