from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
water = list(map(int, input().split()))
queue = deque()
visited = dict()

for i in water:
    queue.append(i)
    visited[i] = 0

while queue:
    if k <= 0:
        break

    now = queue.popleft()
    
    for next in [now + 1, now - 1]:
        if next not in visited and k > 0:
            visited[next] = visited[now] + 1
            k -= 1
            queue.append(next)

res = 0
for k, v in visited.items():
    res += v

print(res)