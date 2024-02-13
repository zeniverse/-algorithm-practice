from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
start, end = map(int, input().split())
start -= 1
end -= 1

def bfs():
    queue = deque([start])
    visited = [-1] * n
    visited[start] = 0

    while queue:
        now = queue.popleft()

        # 오른쪽으로 이동
        for i in range(now, n, arr[now]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[now] + 1

                if i == end:
                    return visited[i]


        # 왼쪽으로 이동
        for i in range(now - arr[now], -1, -arr[now]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[now] + 1

                if i == end:
                    return visited[i]
                
    return -1

print(bfs())

