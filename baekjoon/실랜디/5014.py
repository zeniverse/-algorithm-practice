from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    arr[v] = 0

    while queue:
        x = queue.popleft()
        if x == g:
            return arr[x]

        for nx in (x + u, x - d):
            if 0 < nx <= f and arr[nx] == -1:
                arr[nx] = arr[x] + 1
                queue.append(nx)

    return "use the stairs"

f, s, g, u, d = map(int, input().split())
arr = [-1 for _ in range(f + 1)]
print(bfs(s))
