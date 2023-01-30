from collections import deque

distance = [-1] * 1_000_001

def bfs(x, y, n):
    queue = deque()
    distance[x] = 0
    queue.append(x)

    while queue:
        x = queue.popleft()
        print(x)

        if 0 <= x + n <= 1_000_000 and distance[x + n] == -1:
            distance[x + n] = distance[x] + 1
            queue.append(x + n)
        
        if 0 <= x * 2 <= 1_000_000 and distance[x * 2] == -1:
            distance[x * 2] = distance[x] + 1
            queue.append(x * 2)

        if 0 <= x * 3 <= 1_000_000 and distance[x * 3] == -1:
            distance[x * 3] = distance[x] + 1
            queue.append(x * 3)


def solution(x, y, n):
    bfs(x, y, n)

    return distance[y]

    

x, y, n = 10, 40, 5
print(solution(x, y, n))