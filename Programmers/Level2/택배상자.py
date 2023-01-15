from collections import deque

order = [5, 4, 3, 2, 1]

def solution(order):
    res = []
    num = 1
    sub = deque([])

    for i in order:
        while num <= i:
            sub.appendleft(num)
            num += 1

        if sub[0] == i:
            res.append(sub.popleft())
        else:
            break
        

    return len(res)

print(solution(order))