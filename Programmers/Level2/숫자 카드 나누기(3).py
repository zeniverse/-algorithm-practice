import math
from functools import reduce

# 철수, 영희
arrayA, arrayB = [14, 35, 119], [18, 30, 102]

def check(num, arr):
    for i in arr:
        if i % num == 0:
            return 0
    return num

def solution(arrayA, arrayB):
    arrayA, arrayB = list(set(arrayA)), list(set(arrayB))

    gcd_a = reduce(math.gcd, arrayA)
    gcd_b = reduce(math.gcd, arrayB)

    gcd_a = check(gcd_a, arrayB)
    gcd_b = check(gcd_b, arrayA)

    return max(gcd_a, gcd_b)

print(solution(arrayA, arrayB))