
a = 7
b = 20

def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a

def calc(n):
    res = set()
    d = 2

    while d <= n:
        if n % d == 0:
            res.add(d)
            n = n / d
        else:
            d += 1
    
    return res

def solution(a, b):
    num = gcd(a, b)

    b = b // num
    arr = calc(b)

    if arr - {2, 5}:
        return 2
    else:
        return 1

    

print(solution(a, b))