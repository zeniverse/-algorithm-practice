import math

n = 2
m = 5

def solution(n, m):
    return [math.gcd(n, m), (n * m) / math.gcd(n, m)]

print(solution(n, m))