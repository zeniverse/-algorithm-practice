from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))

    while queue:
        i, j = queue.popleft()
        if i == y:
            return j
        
        for k in (i * 3, i * 2, i + n):
            if k <= y:
                queue.append((k, j + 1))

    return -1

x, y, n = 10, 40, 5
print(solution(x, y, n))