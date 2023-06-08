import math

def solution(n, a, b):
    res = 1

    if a > b:
        a, b = b, a

    while True:
        if a % 2 == 1 and b == a + 1:
            break

        a = math.ceil(a/2)
        b = math.ceil(b/2)
        res += 1

    return res

n = 8
a = 4
b = 7

print(solution(n, a, b))

