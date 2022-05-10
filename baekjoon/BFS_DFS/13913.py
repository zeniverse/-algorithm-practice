from collections import deque

def bfs(v):
    global res

    queue = deque([v])

    while queue:
        now_pos = queue.popleft()

        if now_pos == k:
            print(arr[now_pos])

            while now_pos != n:
                res.append(now_pos)
                now_pos = path[now_pos]

            res.append(n)
            print(*res[::-1])
            return

        for next_pos in [now_pos + 1, now_pos - 1, now_pos * 2]:
            if 0 <= next_pos < max and not arr[next_pos]:
                arr[next_pos] = arr[now_pos] + 1
                queue.append(next_pos)
                
                path[next_pos] = now_pos

n, k = map(int ,input().split())
max = 100_001
arr = [0] * max
path = [0] * max
res = []

bfs(n)