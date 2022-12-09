
a, b, n = 2, 1, 20

def solution(a, b, n):
    res = 0

    while n >= a:
        res += (n // a) * b
        n = (n // a) * b + (n % a)

    return res

print(solution(a, b, n))