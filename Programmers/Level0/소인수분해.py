
n = 420

def solution(n):
    res = set()
    d = 2

    while d <= n:
        if n % d == 0:
            res.add(d)
            n = n / d
        else:
            d += 1
    
    return sorted(list(res))


print(solution(n))
