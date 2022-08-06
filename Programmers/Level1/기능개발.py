from collections import deque
import math

def solution(progresses, speeds):
    cnt = 0
    res = []
    new = deque()

    for i, j in zip(progresses, speeds):
        new.append(math.ceil((100 - i) / j))

    pivot = new[0]

    while new:
        v = new.popleft()
        if v > pivot:
            res.append(cnt)
            cnt = 1
        else:
            cnt += 1
        pivot = max(pivot, v)

    res.append(cnt)

    return res