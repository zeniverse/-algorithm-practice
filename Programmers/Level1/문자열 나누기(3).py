from collections import deque

s = "banana"

def solution(s):
    res = 0

    queue = deque(s)

    while queue:
        a, b = 1, 0
        x = queue.popleft()

        while queue:
            n = queue.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                res += 1
                break
    if a != b:
        res += 1

    return res
        

print(solution(s))