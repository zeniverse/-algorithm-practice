n = 20

def solution(n):
    res = 0

    for i in range(1, n + 1):
        if n % i == 0:
            res += 1

    return res

print(solution(n))