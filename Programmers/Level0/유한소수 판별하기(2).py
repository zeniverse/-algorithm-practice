from math import gcd

a = 7
b = 20

def solution(a, b):
    b = b // gcd(a, b)

    while b % 2 == 0:
        b //= 2
    
    while b % 5 == 0:
        b //= 5

    return 1 if b == 1 else 2
    

print(solution(a, b))