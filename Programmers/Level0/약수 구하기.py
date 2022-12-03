
n = 29

def solution(n):
    res = set()

    for i in range(1, n//2 + 2):
        if n % i == 0:
            res.add(i)
            res.add(n//i)

    res = list(res)
    res.sort()

    return res


print(solution(n))
