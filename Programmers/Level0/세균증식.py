n = 7
t = 15

def solution(n, t):
    res = 0

    while t > 0:
        n *= 2
        t -= 1

    return n

print(solution(n, t))
