from collections import deque

def solution(n, m, section):
    res = 0
    section = deque(section)

    while section:
        start = section.popleft()

        while section:
            if section[0] >= start + m:
                 break
            section.popleft()
        res += 1

    return res

n, m = 16, 4
section = [2, 3, 15, 16]

print(solution(n, m, section))
