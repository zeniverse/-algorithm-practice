from math import gcd
from functools import reduce

# 철수, 영희
arrayA, arrayB = [14, 35, 119], [18, 30, 102]


def solution(arrayA, arrayB):
    res = []
    
    gcd_A = reduce(gcd, arrayA)
    gcd_B = reduce(gcd, arrayB)

    if all(i % gcd_B for i in arrayA):
        res.append(gcd_B)
    
    if all(i % gcd_A for i in arrayB):
        res.append(gcd_A)

    return max(res) if res else 0

print(solution(arrayA, arrayB))