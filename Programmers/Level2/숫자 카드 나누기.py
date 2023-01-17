from math import gcd

# 철수, 영희
arrayA, arrayB = [14, 35, 119], [18, 30, 102]


def solution(arrayA, arrayB):
    res = []

    gcd_A, gcd_B = arrayA[0], arrayB[0]
    for num_A , num_B in zip(arrayA[1:], arrayB[1:]):
        gcd_A = gcd(gcd_A, num_A)
        gcd_B = gcd(gcd_B, num_B)

    for i in arrayA:
        if i % gcd_B == 0:
            break
    else:
        res.append(gcd_B)
    
    for i in arrayB:
        if i % gcd_A == 0:
            break
    else:
        res.append(gcd_A)
    

    return max(res) if res else 0

print(solution(arrayA, arrayB))