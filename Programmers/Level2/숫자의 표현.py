
n = 15

def solution(n):
    res = 0

    d = 1

    while n > 0:
        if n  % d == 0:
            res += 1

        n -= d
        d += 1

    return res

print(solution(n))
